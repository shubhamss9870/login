from django.contrib import admin
from django.urls import path
from .import views, Hod_views,student_views, teacher_views
urlpatterns = [
    path('', views.first_page, name= 'index'),
    path('sign_up', views.sign_ups, name = "sign_up"),
    path('log_in', views.login, name="log_in"),
    path('log_out', views.logout, name="log_out"),

    #login path
    path('logs_in', views.logsin, name= "log_in")
]
