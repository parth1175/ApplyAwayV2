from demoapp.models import EBooksModel
from django import forms

class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = ('title', 'pdf',)