# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm

# To immediatedly go to the post_detail page for our newly created blog post
from django.shortcuts import redirect




# Create your views here.
def post_list(request):
	# Including -> Publishing Post by using Queryset
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})


def sys_info_page(request):
	return render(request, 'blog/sys_info_page.html', {})


# Returns details about a post when clicked on.
def post_detail(request, pk):
	#Post.objects.get(pk=pk)
	#
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})


# Forms for new post
def post_new(request):
	
	if request.method == "POST":
		# Passing form fields(title, text) (provided by the author) to 
		# PostForm Form.
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)		#redirect to the above class- post_detail

	else:	
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form':form})


# To edit any previous Post
def post_edit(request, pk):
	# We get the Post model we want to edit by bellow statement
	post = get_object_or_404(Post, pk=pk)


	if request.method == 'POST':
		# We create a form --> passing this 'post' as an instance
		# This way we are kind of indirectly overwriting the 'post'(determined by its pk)
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form =  PostForm(instance=post)

	return render(request, 'blog/post_edit.html', {'form':form})	