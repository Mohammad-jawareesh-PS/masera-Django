
from django import forms
from .models import *


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'input1','placeholder':'الاسم'}),
            'email': forms.EmailInput(attrs={'class':'input1','placeholder':'البريد الاكتروني'}),
            'Subject': forms.TextInput(attrs={'class':'input1','placeholder':'الموضوع'}),
            'message': forms.Textarea(attrs={'class':'input1','placeholder':'الرسالة'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'البريد الاكتروني'}),
            'username': forms.TextInput(attrs={'placeholder':' الاسم'}),
            'password': forms.PasswordInput(attrs={'placeholder':'كلمه المرور'}),

        }

