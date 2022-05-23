from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
    nu = forms.IntegerField(label="Int 1")
    nu_2 = forms.IntegerField(label="Int 2")


