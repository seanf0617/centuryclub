from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class RecordForm(forms.Form):
    date = forms.CharField(label='Date:', max_length=20)