from django import forms
from .models import Students


class AddStudentsForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)

class AddStudentModel(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Students