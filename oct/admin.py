from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import OCT_Image


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(OCT_Image)