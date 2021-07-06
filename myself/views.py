from .models import GuestLog
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.

def index(request):
    guestform = GuestForm()
    commentform = CommentForm()
    log = GuestLog.objects.all()
    comment = GuestComment.objects.all()
    context = { 'log' : log, 'commentlog': comment, 'guestform': guestform, 'commentform': commentform }
    return render(request, 'myself/index.html', context)

def bookadd(request):
    if request.method == 'GET':
        form = GuestForm()
    elif request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            guestbook = form.save(commit=False) 
            guestbook.save()
    return redirect('index')

def commentadd(request, log_id):
    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            guestcomment = form.save(commit=False) 
            guestcomment.logID = log_id
            guestcomment.save()
    return redirect('index')