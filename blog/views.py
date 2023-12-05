from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import BlogPost
from django.http import HttpResponseRedirect
from django.utils import timezone




def blog_list_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)
def blog_detail_view(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    context={"post":post}
    return render(request,"blog/detail.html",context)
def blog_create_view(request):
    if request.method=="POST":
        blog=BlogPost.objects.create(
            title=request.POST.get("title"),
            textarea=request.POST.get("textarea"),
            date=timezone.now()
            )
        return HttpResponseRedirect("/blog/")
    else:
        return render(request,"blog/create.html")
    