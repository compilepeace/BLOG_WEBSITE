from django import forms
from .models import Post

# To immediatedly go to the post_detail page for our newly created blog post
from django.shortcuts import redirect

# 'PostForm' --> name of our form
class PostForm(forms.ModelForm):

	class Meta:
		# Here, we tell this model which model is used to create the form
		model = Post
		fields = ('title', 'text',)