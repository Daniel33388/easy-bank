from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.order_by('-date')
    ctx = {
        'posts': posts
    } 
    return render(request, 'blog/blog.html', ctx)
