from django import forms

class LoginForm(forms.form)
username=forms.Charfield()
password = forms.Charfield(widget=forms.PasswordInput)
