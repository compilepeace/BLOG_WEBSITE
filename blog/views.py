# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def post_list(request):
	# Including -> Publishing Post by using Queryset
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def sys_info_page(request):
	return render(request, 'blog/sys_info_page.html', {})


def post_detail(request, pk):
	#Post.objects.get(pk=pk)
	#
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})