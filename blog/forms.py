from django import forms
from .models import Post

class PostForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(max_length=2000, widget = forms.Textarea())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']
