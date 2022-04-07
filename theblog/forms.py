from django import forms
from .models import Post, Category

#choices = [('coding', 'coding'), ('Security', 'Security'), ('Normal', 'Normal'),]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'(Please type the title of your blog)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'(Please TAG your blog)'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'(Please choose your name...)'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder':'(Please choose a category.)'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'(Type in your blog. Enjoy!!!)'}),
        }