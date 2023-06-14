from django.shortcuts import render, redirect
from .models import Post
from .forms import CreateNewPost

# Create your views here.

def index(request):
    posts = list(Post.objects.values())
    return render(request, 'index.html', {'posts': posts})

def newPost(request):
    if request.method == 'GET':
        return render(request, 'newPost.html', {'form': CreateNewPost()})
    else:
        Post.objects.create(title=request.POST['title'], text=request.POST['text'])
        return redirect('/')

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

def editPost(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        form = CreateNewPost(instance=post)
        return render(request, 'editPost.html', {'form' : form})
    else:
        post = Post.objects.get(id=id)
        form = CreateNewPost(request.POST, instance=post)
        form.save()
        return redirect('/')

def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')