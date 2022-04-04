from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'(Please type the title of your blog)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'(Please TAG your blog)'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'(Please choose your name...)'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'(Type in your blog. Enjoy!!!)'}),
        }