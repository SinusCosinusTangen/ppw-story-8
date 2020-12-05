from django.http import JsonResponse
from django.http import request
from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def index(request):
    response = {}
    return render(request, 'index.html', response)

def data(request):
    url = "https://www.googleapis.com/books/v1/volumes?q=" + request.GET['q']
    ret = requests.get(url)
    data = json.loads(ret.content)
    return JsonResponse(data, safe=False)