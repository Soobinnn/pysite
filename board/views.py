from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from board.models import Board

from user.models import User


def list(request):
    board = Board.objects.all().order_by('-group_no', 'order_no')

    paginator = Paginator(board, 10)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    page_numbers_range = 10
    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]

    data = {'board': board, 'page_obj': page_obj, 'page_range': page_range}
    return render(request, 'board/list.html', data)

def write(request):
    if request.method == "GET":
        return render(request, 'board/write.html')

    if request.method == "POST":
        board = Board()

        board.title = request.POST['title']
        board.contents = request.POST['contents']
        board.hit = request.POST['hit']
        board.group_no = request.POST['group_no']
        board.order_no = request.POST['order_no']
        board.depth = request.POST['depth']
        board.no = User.objects.get(no=request.session['authuser']['no'])
        if board.group_no == '':
            maxgroupno = Board.objects.aggregate(Max('group_no'))
            board.group_no = maxgroupno['group_no__max']+1
            print(board.group_no)
            board.save()
        else:
            board.save()

        return HttpResponseRedirect('/board/')

def view(request):
    board = Board.objects.get(board_no=request.GET['no'])
    board.hit += 1

    board.save()
    data = {'board': board}
    return render(request, 'board/view.html', data)

def reply(request):
    if request.method == "GET":
        groupno = request.GET['g']
        orderno = request.GET['o']
        depth = request.GET['d']

        orderno = int(groupno)+1
        depth = int(depth)+1
        print(groupno)
        print(orderno)
        print(depth)
        replywrite = {'groupno': groupno, 'orderno': orderno, 'depth': depth}
    return render(request, 'board/write.html', replywrite)

def modify(request):
    board = Board.objects.get(board_no=request.GET['no'])
    data = {
        'board': board
    }

    return render(request, 'board/modify.html', data)

def modifysuccess(request):
    board = Board.objects.get(board_no=request.POST['board_no'])
    board.title = request.POST['title']
    board.contents = request.POST['contents']
    board.save()


    return HttpResponseRedirect('/board/view?no='+request.POST['board_no'])

def delete(request):
    board = Board.objects.get(board_no=request.GET['no'])
    board.delete()
    return HttpResponseRedirect('/board')