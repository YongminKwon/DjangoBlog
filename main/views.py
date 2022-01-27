from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})

def posting(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('mainphoto'):
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.FILES.get('mainphoto'),
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST.get('mainphoto'),
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.postname = post.postname
        post.contents = request.POST.get('contents')
        post.mainphoto = request.FILES.get('mainphoto')
        post.save()
        return redirect('blog')
    return render(request, 'main/edit_post.html', {'Post': post})
