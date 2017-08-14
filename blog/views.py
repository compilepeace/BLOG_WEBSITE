# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {})