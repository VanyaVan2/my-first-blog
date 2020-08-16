from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Task

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def tasks_list(request):
    '''task = get_object_or_404(Task, pkT)'''
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/tasks_list.html', {'tasks': tasks})

    

