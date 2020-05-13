from rest_framework import serializers
from .models import SourceLinks

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceLinks
        fields = '__all__'
    
    

