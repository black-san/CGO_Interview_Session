from django import forms

class createForm(forms.Form):
    x = forms.IntegerField(label="X", widget=forms.TextInput(attrs={'placeholder': 'Example: 5'}))
    a = forms.CharField(label="A", widget=forms.TextInput(attrs={'placeholder': 'Example: 1, 2, 3, 5, 4'}))
    
