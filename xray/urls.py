from django.urls import path
from . import views

urlpatterns = [
    path('uploadXRAY/',views.XRAY_Upload_View.as_view(),name='xray-upload'),
    path('download-sample/',views.XRAY_DownloadSample_View,name='oct-download-sample')
]
