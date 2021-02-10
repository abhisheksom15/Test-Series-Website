from django.shortcuts import render,get_object_or_404,get_list_or_404
from django import forms
from question_app.forms import UserForm,UserProfileInfoForm,SkillForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from question_app.models import UserProfileInfo,User,questions,result_user,Test_Information,Test_Marks,skills_info,levels
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.generic.edit import View,UpdateView
from question_app.models import UserProfileInfo
from taggit.models import Tag
import os
import random
# Create your views here.
class education_update(UpdateView):
    widgets = {
        'Last_Highest_Education': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Recent Highest Education'}),
        'School_or_College_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Recent School/College Name'}),
        'Education_Percentage': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Percentage'}),
    }
    fields=('Last_Highest_Education','School_or_College_Name','Education_Percentage','branch_of_graduation')
    model=UserProfileInfo
    template_name = 'UserProfileInfo_updateform.html'
@login_required
def skills_update(request):
    all_skills=skills_info.objects.all().filter(user=request.user)
    form=SkillForm(request.POST)

    print(form)
    if request.method=="POST":
        print(request.user)

        if form.is_valid():
            skills_details=form.save(commit=False)
            skills_details.user=request.user
            print("done")
            skills_details.save()
    context={
        'form': form,
        'all_skills':all_skills,
    }
    return render(request,'skills_update.html',context)
class profile_update(UpdateView):
    fields=('Address','phone_number','Govt_ID_type','Govt_ID_number')
    model=UserProfileInfo
    template_name = 'UserProfileInfo_updateform.html'
    #success_url = reverse('question_bank:welcomes')
#def update_education(request):
#    return render(request,"Update_Education.html")
def about(request):
    return render(request,"about.html")
def welcome(request):
    ti=Test_Information.objects.all()
    if (request.user.is_authenticated):
        user_info=get_object_or_404(UserProfileInfo,user=request.user)
        return render(request,"welcome.html",{'ti':ti,'user_info':user_info})
    #Welcome_template=os.path.join("question_app","welcome.html")
    return render(request,"welcome.html",{'ti':ti})
def description(request,pk):
    test=get_object_or_404(Test_Information,pk=pk)
    return render(request,'description.html',{'test':test})
def register(request):

    registered=False

    if(request.method=="POST"):
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save(commit=False)
            try:
                validate_password(user.password, user)
            except ValidationError as e:
                user_form.add_error('password', e)
                return render(request,'Registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered,"Warning":"Password not strong"})
            user.set_password(user.password)
            user.save()
            if(user):
                if(user.is_active):
                    login(request,user)
                    user_test=user
            profile=profile_form.save(commit=False)
            profile.user=user

            if('profile_pic' in request.FILES):
                profile.profile_pic=request.FILES['profile_pic']
            #Updating Percentage of profiles
            education=0
            sum_education=0
            if(profile.School_or_College_Name!=""):
                education+=1
            sum_education+=1
            if(profile.Education_Percentage!=0):
                education+=1
            sum_education+=1

            if(profile.branch_of_graduation!=""):
                education+=1
            sum_education+=1

            if(profile.Last_Highest_Education!=""):
                education+=1
            sum_education+=1
            profile.education_filled=int((100*education)//sum_education)
            #Completed the Education % part
            skills=0
            sum_skills=0
            sum_skills+=1
            profile.Skills_filled=int((100*skills)//sum_skills)
            #Completed the skills part
            profile_ver=0
            sum_profile=0
            if(profile.Address!=""):
                profile_ver+=1
            sum_profile+=1
            if(profile.phone_number!=0):
                profile_ver+=1
            sum_profile+=1
            if(profile.Govt_ID_type!=""):
                profile_ver+=1
            sum_profile+=1
            if(profile.Govt_ID_number!=""):
                profile_ver+=1
            sum_profile+=1
            profile.Prfoile_verification_filled=int((100*profile_ver)//sum_profile)
            #print(self.Prfoile_verification_filled)
            profile.save()
            registered=True
            user=authenticate(username=user.username,password=user.password)
            if(user):
                if(user.is_active):
                    login(request,user)
                    user_test=user
            HttpResponseRedirect(reverse('welcome'))
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'Registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))
@login_required
def question_test(request,user_pk,test_pk,count=0):
    question_paper=get_object_or_404(Test_Information,pk=test_pk)
    question_list=""
    answer_list=""
    count=int(count)+1
    number_of_questions=question_paper.number_of_questions
    if(request.method=="POST"):
        answer=request.POST.get("Answer")
        ans
    if(count==int(number_of_questions)+1):
        return HttpResponseRedirect(reverse("complete"))
    else:
        all_question=question_paper.question_number.all()
        curr_question=all_question[count-1]
        return render(request,"queqstion_paper.html",{"question":curr_question,"count":count,"Test":question_paper})
@login_required
def complete(request):
    return render(request,"complete.html")
def user_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if(user):
            if(user.is_active):
                login(request,user)
                user_test=user
                return HttpResponseRedirect(reverse('welcome'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("someone tried to access account unauthenically and failed")
            print("Username {} and password {}".format(username,password))
            return render(request,"login.html",{"error_message":"● User Name or Password is Invalid"})
    else:
        return render(request,'Login.html',{})
