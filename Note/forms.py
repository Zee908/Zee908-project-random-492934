from django import forms
from .models import Note
class ContentForm(forms.Form):
    title=forms.CharField(max_length=30,)
    content=forms.CharField(max_length=500,)


class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields = "__all__"

