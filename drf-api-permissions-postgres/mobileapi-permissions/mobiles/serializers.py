
from rest_framework import serializers

from .models import Mobile,Post
class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mobile
       
        fields='__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields='__all__'
