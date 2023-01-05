from django import forms
from diary.models import Page

class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title', 'content', 'feeling', 'score', 'dt_created']
        