from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    date_of_birth = models.DateField()
    Address=models.CharField(max_length=200)
    Tenth="10th Class"
    Tweleth="12th Class"
    grad="Graduation"
    post="Post Graduation"
    Doctorate="Doctorate"
    education_filled=models.IntegerField(default=0)
    edu_choices=((Tenth,'10th Class'),(Tweleth,'12th Class'),(grad,'Graduation'),(post,'Post Graduation'),(Doctorate,'Doctorate'))
    Last_Highest_Education=models.CharField(choices=edu_choices,max_length=20)
    School_or_College_Name=models.CharField(max_length=100)
    Education_Percentage=models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    branch_of_graduation=models.CharField(max_length=50)
    Skills_filled=models.IntegerField(default=0)
    Main_Hobbies=TaggableManager()
    PAN_number='PAN card'
    Aadhar_number='Aadhar card'
    Driving_License='Driving License'
    Voter_ID='Voter ID'
    ID_choices=((PAN_number,'PAN card'),(Aadhar_number,'Aadhar number'),(Driving_License,'Driving License'),(Voter_ID,'Voter_ID'))
    Govt_ID_type=models.CharField(choices=ID_choices,max_length=20)
    Govt_ID_number=models.CharField(max_length=30)
    Prfoile_verification_filled=models.IntegerField(default=0)
    def get_absolute_url(self):
        education=0
        sum_education=0
        if(self.School_or_College_Name!=""):
            education+=1
        sum_education+=1
        if(self.Education_Percentage!=0):
            education+=1
        sum_education+=1

        if(self.branch_of_graduation!=""):
            education+=1
        sum_education+=1

        if(self.Last_Highest_Education!=""):
            education+=1
        sum_education+=1
        self.education_filled=int((100*education)//sum_education)
        #Completed the Education % part
        skills=0
        sum_skills=0
        skills+=1
        sum_skills+=1
        self.Skills_filled=int((100*skills)//sum_skills)
        #Completed the skills part
        profile=0
        sum_profile=0
        if(self.Address!=""):
            profile+=1
        sum_profile+=1
        if(self.phone_number!=0):
            profile+=1
        sum_profile+=1
        if(self.Govt_ID_type!=""):
            profile+=1
        sum_profile+=1
        if(self.Govt_ID_number!=""):
            profile+=1
        sum_profile+=1
        self.Prfoile_verification_filled=int((100*profile)//sum_profile)
        print(self.Prfoile_verification_filled)
        self.save()
        return reverse('welcome')
    def __str__(self):
        return self.user.username
class levels(models.Model):
    skill_level=models.CharField(max_length=100)
    def __str__(self):
        return self.skill_level
class skills_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skills=models.CharField(max_length=100)
    level=models.ForeignKey(levels,on_delete=models.CASCADE)
    def __str__(self):
        return self.skills
class education_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Tenth="10th Class"
    Tweleth="12th Class"
    grad="Graduation"
    post="Post Graduation"
    Doctorate="Doctorate"
    education_filled=models.IntegerField(default=0)
    edu_choices=((Tenth,'10th Class'),(Tweleth,'12th Class'),(grad,'Graduation'),(post,'Post Graduation'),(Doctorate,'Doctorate'))
    Education_type=models.CharField(choices=edu_choices,max_length=20)
    School_or_College_Name=models.CharField(max_length=100)
    Education_Percentage=models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
        return user+Education_type+School_or_College_Name
class questions(models.Model):
    Mathematics="Mathematics"
    Quantative_Aptitude="Quantative Aptitude"
    Reasoning="Reasoning"
    English="English"
    cat_choice=((Mathematics,"Mathematics"),(Quantative_Aptitude,"Quantative Aptitude"),(Reasoning,"Reasoning"),(English,"English"))
    Category=models.CharField(choices=cat_choice,max_length=50)
    Difficulty_level=models.PositiveSmallIntegerField()
    Question=models.CharField(max_length=512)
    Option_A=models.CharField(max_length=256)
    Option_B=models.CharField(max_length=256)
    Option_C=models.CharField(max_length=256)
    Option_D=models.CharField(max_length=256)
    A="A"
    B="B"
    C="C"
    D="D"
    option_choice=((A,"A"),(B,"B"),(C,"C"),(D,"D"))
    Answer=models.CharField(choices=option_choice,max_length=10)
    Answer_Description=models.CharField(max_length=512)
    def __str__(self):
        return self.Question
class result_user(models.Model):
    user_result=models.OneToOneField(User,on_delete=models.CASCADE)
    marks=models.CharField(max_length=2048)
    date_of_exam= models.DateTimeField(auto_now_add=True)
    quest_list=models.CharField(max_length=2048,default="")
    exam_name=models.CharField(max_length=256)
    def __str__(self):
         return self.user_result.username
class Test_Information(models.Model):
    Test_name=models.CharField(max_length=256)
    Position=models.CharField(max_length=256)
    Difficulty_level=models.PositiveIntegerField()
    Description=models.CharField(max_length=512)
    number_of_questions=models.PositiveIntegerField()
    question_number=models.ManyToManyField(questions)
    def __str__(self):
        return self.Test_name
class Test_Marks(models.Model):
    user_name=models.ForeignKey(result_user,on_delete=models.CASCADE)
    Test_name=models.ForeignKey(Test_Information,on_delete=models.CASCADE)
    cm_marks=models.PositiveSmallIntegerField()
    cm_position=models.CharField(max_length=256)
    def __str__(self):
        return self.user_name.user_result.username
