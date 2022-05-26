from django.urls import path, include

from django.contrib.auth import views as auth_vews

from . import views

app_name='common'

urlpatterns=[
    path('covid/',views.covid, name='covid')
]