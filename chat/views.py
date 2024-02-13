import json

from django.shortcuts import render
from django.http import HttpResponse


chats = []


def index(request):
    context = {'chats': chats}
    return render(request, 'chat/index.html', context)


def get_chats(request):
    return HttpResponse(json.dumps({'chats': chats}))


def post_chat(request):
    chat = request.GET['message']
    chats.append(chat)
    return HttpResponse()