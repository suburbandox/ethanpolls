from django.shortcuts import render
from django.http import JsonResponse
from .models import Cocktail
import requests
import markdown

def cocktailindex(request):
    url= request.build_absolute_uri("/cocktails/api") 
    response=requests.get(url)
    data =response.json()
    context={"data":data}
    for result in data['results']:
        result["recipe"] = markdown.markdown(result["recipe"]) 
    return render(request,"cocktails/index.html",context)

def cocktailapi(request):
    cocktails = Cocktail.objects.all()
    return JsonResponse({"results":[
        {
            'name':cocktail.name,
            "root_cocktail":cocktail.root_cocktail,
            "primary_spirit":cocktail.primary_spirit,
            "recipe":cocktail.recipe,
            
         }for cocktail in cocktails
    ]})