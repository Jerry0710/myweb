from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        # return render(request, 'post.html', locals())
        return redirect('/')
