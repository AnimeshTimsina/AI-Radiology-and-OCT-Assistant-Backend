from django.urls import path
from . import views

urlpatterns = [
    path('links/',views.LinksView.as_view(),name='desc-links')
]
