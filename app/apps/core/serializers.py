from rest_framework import serializers
from .models import (
    CodeQuality,
    Site
)


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class CodeQualitySerializer(serializers.ModelSerializer): 
    
    site = SiteSerializer(many=True, required=False)
    
    class Meta:
        model = CodeQuality
        fields = ["pk", "name", "site"]
