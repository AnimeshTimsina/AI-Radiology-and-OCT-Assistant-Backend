from django.urls import path
from . import views

urlpatterns = [
    path('download-sample/',views.XRAY_DownloadSample_View,name='oct-download-sample')
]
