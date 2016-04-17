from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    view = 'home'
    temp = get_template('index.html')
    html = temp.render(Context({'user': 'хуюзер'}))
    return HttpResponse(html)