# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

# Create your views here.

def index(request):
	context = {
		'time': strftime('%b %d, %Y %I:%M %p', localtime())
	}
	return render(request, 'clock/index.html', context)