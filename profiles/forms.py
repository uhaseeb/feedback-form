from django import forms


class ProfileForm(forms.Form):
    image = forms.FileField(label="Please upload an image ")


