from django import forms 
from .models import Registration


class RegistrForm(forms.Form):
    uid=forms.IntegerField(widget=forms.NumberInput(attrs={"plceholder":"enter your uid","class":"form-control"}))
    name=forms.CharField(widget=forms.TextInput(attrs={"plceholder":"enter your name","class":"form-control"}))
    phno=forms.IntegerField(widget=forms.NumberInput(attrs={"plceholder":"enter your experince","class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"plceholder":"enter your Emai id","class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        ex=cleaned_data.get('phno')
        if ('length')<10:
            msg="Mobile number invalid"
            self.add_error('phno',msg)


