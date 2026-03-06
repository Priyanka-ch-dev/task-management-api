from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.utils.timezone import now

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self,validated_data):

        user = User.objects.create_user(

        username = validated_data['username'],
        email = validated_data['email'],
        password = validated_data['password']

        )

        return user
    
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_by']

    def validate_title(self,value):

        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")

        return value


    def validate_due_date(self,value):

        if value < now().date():
            raise serializers.ValidationError("Due date cannot be in the past")

        return value