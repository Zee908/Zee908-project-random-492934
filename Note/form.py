from django import forms
class Contact(forms.From):
    full_name=forms.CharField(max_length=50,required=True)
    phone_number=forms.CharField(max_length=11,required=True)
    email= forms.EmailField(required=False)