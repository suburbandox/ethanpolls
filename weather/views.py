from django.shortcuts import render
import urllib
import json

def weather_index(request):
    
    if "rat" in request.GET and"atooi"in request.GET:
        rat =request.GET["rat"]
        atooi =request.GET["atooi"]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={rat}&longitude={atooi}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m" 
        response = urllib.request.urlopen(url).read()
        data = json.loads(response)
        celsius = data['current']["temperature_2m"]
        fahrenheit= celsius *1.8 +32 
        context = {'temp':fahrenheit}
    else:
        context = {}
    return render(request,"weather/index.html",context)