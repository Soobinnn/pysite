# Generated by Django 2.2.2 on 2019-06-24 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('hit', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now=True)),
                ('group_no', models.IntegerField()),
                ('order_no', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]