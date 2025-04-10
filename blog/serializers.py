from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Blog
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username','email','password']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user