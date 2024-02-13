from django.shortcuts import render

# Create your views here.
def chat_home(request):
    # posts = BlogPost.objects.all().order_by("-date")
    return render(request, "chat/index.html")

