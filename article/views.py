from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article

def home(request):
    view = 'home'
    temp = get_template('index.html')
    html = temp.render(Context({'user': 'хуюзер'}))
    return HttpResponse(html)


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})