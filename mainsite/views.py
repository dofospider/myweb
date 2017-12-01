# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

from datetime import datetime

from django.template.loader import get_template
# Create your views here.


def index(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)


def homepage(request):
    template = get_template('index_old.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)

    except:
        return redirect('/')


def home(request):
    template = get_template('home.html')
    html = template.render()
    return HttpResponse(html)
