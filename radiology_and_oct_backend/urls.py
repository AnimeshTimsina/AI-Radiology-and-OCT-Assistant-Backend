from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oct/',include('oct.urls')),
    path('xray/',include('xray.urls')),
    path('desc/',include('project_description.urls')),
    path('mail/',include('subscribe.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
