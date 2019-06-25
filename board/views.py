from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board

from user.models import User


def list(request):
    board = Board.objects.all().order_by('-group_no', 'order_no')

    # for t in board:


    data = {'board': board}
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
    data ={'board': board}
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

    return render(request, 'board/modify.html',data)

def modifysuccess(request):
    board = Board.objects.get(board_no=request.POST['board_no'])
    board.title = request.POST['title']
    board.contents = request.POST['contents']
    board.save()


    return HttpResponseRedirect('/board/view?no='+request.POST['board_no'])
