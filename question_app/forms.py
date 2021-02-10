from django import forms
from django.contrib.auth.models import User
from question_app.models import UserProfileInfo,skills_info,levels
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from question_bank import settings


class UserForm(forms.ModelForm):
    #password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        error_css_class = "error"
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'E-mail ID'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
        }
        fields=( 'username','email','password','first_name','last_name' )

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        error_css_class = "error"
        model = UserProfileInfo
        #date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        #date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y',attrs={'type':'date','class': 'form-control'}), input_formats=settings.DATE_INPUT_FORMATS,)
        #date_of_birth = forms.DateField(widget=AdminDateWidget)
        widgets = {
            'date_of_birth' : forms.TextInput(attrs={'type':'date','class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mobile Number'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Addres here...'}),
            'school_10th': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your High School Name'}),
            'percentage_10th': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'percentage of High School'}),
            'school_12th': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Intermediate/Diploma School Name'}),
            'percentage_12th': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Percentage of Intermediate/Diploma'}),
            #'graduation': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Graduation School Name'}),
            #'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
        }
        fields=('phone_number', 'date_of_birth')
class SkillForm(forms.ModelForm):
    class Meta():
        error_css_class = "error"
        model = skills_info
        #date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        #date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y',attrs={'type':'date','class': 'form-control'}), input_formats=settings.DATE_INPUT_FORMATS,)
        #date_of_birth = forms.DateField(widget=AdminDateWidget)
        widgets = {
            'skills': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Skill',}),
            #'level': forms.TextInput(attrs={'class': 'form-control','placeholder':'Rate your Skill',}),
        }
        fields=('skills','level')
