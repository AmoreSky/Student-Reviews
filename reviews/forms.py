from django import forms
from .models import Review
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name','level', 'lecturer_name', 'course_code','review_or_complaint']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px; height:30px'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px; height: 30px'}),
            'level': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px; height: 30px'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px; height:30px; height:30px'}),
            'lecturer_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px;height:30px'}),
            'review_or_complaint': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width:500px'}),
        }

# class SignUpForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','matric_number', 'email', 'password1','password2'



class SignUpForm(UserCreationForm): 
    full_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))    
    matric_number = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))       
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'})) 
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
             

    class Meta:
        model = User
        fields = ('username', 'full_name', 'matric_number', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username']

        self.fields['matric_number']

        self.fields['email']


        self.fields['password1']


        self.fields['password2']
        
