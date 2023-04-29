from django import forms

class StudentForm(forms.Form):
    studentid = forms.CharField(max_length=10)
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=200, required=False)
    phone = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=200, required=False)
    
