from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
    def clean(self):

        return self.cleaned_data
    class Meta:
        model = Blog
        fields = ['title','body','image','tags',]
         