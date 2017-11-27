# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import threeD

from datetime import datetime

from django.template.loader import get_template

# Create your views here.


def maintd(request):
    template = get_template('3d.html')
    alldata = threeD.objects.all()
    number = len(alldata)
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
