from django.shortcuts import render
import os
import requests

RAWG_API_KEY = os.environ["RAWG_API_KEY"]
# Create your views here.
def rawg_index(request):
    url = f'https://rawg.io/api/users/emkline/games?discover=true&ordering=-released&page_size=20&page=1&key={RAWG_API_KEY}'
    response = requests.get(url)
    data = response.json()
    context = {'data':data}
    return render(request,'rawg/index.html',context)
