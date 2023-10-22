from django import forms

class student_form(forms.Form):
    name = forms.CharField(required=False)
    roll = forms.IntegerField(required=False)