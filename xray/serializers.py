from rest_framework import serializers
from .models import XRAY_Image



class XRAY_Image_Serializer(serializers.ModelSerializer):
    class Meta:
        model = XRAY_Image
        fields = ['image']