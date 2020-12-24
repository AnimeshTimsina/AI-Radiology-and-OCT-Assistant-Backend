from rest_framework import serializers
from .models import OCT_Image

class OCT_Image_Serializer(serializers.ModelSerializer):
    class Meta:
        model = OCT_Image
        fields = ['image']
    
    