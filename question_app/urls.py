from django.urls import path
from question_app import views

app_name='question_app'

urlpatterns=[
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),

]
