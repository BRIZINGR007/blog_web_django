from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *
#choices = [('coding','coding'),('sports','sports')]
choices=Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content','category']
        widgets={
            'category':forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('name','body')
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

    