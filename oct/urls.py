from django.urls import path
from . import views

urlpatterns = [
    path('uploadOCT/',views.OCT_Upload_View.as_view(),name='oct-upload'),
    path('download-sample/',views.OCT_DownloadSample_View,name='oct-download-sample')
]
