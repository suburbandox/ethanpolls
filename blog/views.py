from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import BlogPost



def blog_list_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)
def blog_detail_view(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    context={"post":post}
    return render(request,"blog/detail.html",context)