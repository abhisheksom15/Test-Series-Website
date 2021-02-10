from django.contrib import admin
from question_app.models import UserProfileInfo,questions,result_user,Test_Information,Test_Marks,skills_info,levels,education_info
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(questions)
admin.site.register(result_user)
admin.site.register(Test_Information)
admin.site.register(Test_Marks)
admin.site.register(skills_info)
admin.site.register(levels)
admin.site.register(education_info)
