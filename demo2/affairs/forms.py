from django import forms
from .models import Students,Intake,Track


class AddStudentsForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)

class AddStudentModel(forms.ModelForm):
    intakeid = forms.ChoiceField(choices=[(intake.id,intake.intakeName) for intake in Intake.objects.all()])
    trackid = forms.ChoiceField(choices=[(track.id,track.name) for track in Track.objects.all()])
    class Meta:
        fields='__all__'
        model=Students

class AddIntakeModel(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Intake


class AddTrackModel(forms.ModelForm):
    class Meta:
        fields ='__all__'
        model = Track