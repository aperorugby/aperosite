from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
