from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import logout
from .models import BlogPost
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def blog_list_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def blog_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {"post": post}
    return render(request, "blog/detail.html", context)


def blog_create_view(request):
    if request.method == "POST":
        blog = BlogPost.objects.create(
            title=request.POST.get("title"),
            textarea=request.POST.get("textarea"),
            date=timezone.now(),
            creator=request.user if request.user.is_authenticated else None
        )
        return HttpResponseRedirect("/blog/")
    else:
        return render(request, "blog/create.html")

def blog_edit_view(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.textarea = request.POST.get('textarea')
        blog.last_updated = timezone.now()
        if request.user.is_authenticated:
            blog.user = request.user
        else:
            blog.user = None
        blog.save()
        return HttpResponseRedirect(f"/blog/{pk}")
    else:
        context = {"blog": blog}
        return render(request, "blog/edit.html", context)


def blog_signup_view(request):
    if request.method == "POST":
        print('post here', request.POST)
        return HttpResponse('thx 4 signup')
    else:
        return render(request, "blog/signup.html")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "blog/signup.html"


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(f"/blog/")