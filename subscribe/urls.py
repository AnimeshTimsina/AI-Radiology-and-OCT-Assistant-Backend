from django.urls import path
from . import views

urlpatterns = [
    path('send/',views.SendEmailView.as_view(),name='send-email'),
]
