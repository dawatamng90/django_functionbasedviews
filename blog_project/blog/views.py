from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

# create post
def home(request):
    """Display all posts."""
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'blog/home.html',{'posts':posts})

def post_detail(request, post_id):
    """Display a single post."""
    post = get_object_or_404(Post, id=post_id)
    return render(request,'blog/post_detail.html', {'post':post})
 
def add_post(request):
    """Create a new post."""
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'blog/add_post.html', {'form':form})

def update_post(request, post_id):
    """Update an existing post."""
    post = get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance = post)
    return render(request,'blog/update_post.html', {'form':form, 'post':post})

def delete_post(request, post_id):
    """Delete an existing post."""
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')