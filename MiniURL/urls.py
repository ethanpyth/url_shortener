from django.urls import path

from MiniURL import views


app_name = "MiniURL"

urlpatterns = [
    path('', views.form_views, name='forms_views'),
    path('redirect/<str:code>', views.redirections, name='redirections')
]
