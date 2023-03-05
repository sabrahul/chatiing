from rest_framework import serializers
from .models import User,Message

class UserRegisterSerializer(serializers.ModelSerializer):
    # password=serializers.CharField(style={'input_type':'password'})
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['id','name','email','password','password2']

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError('passwords do not match')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=55)
    class Meta:
        model=User
        fields=['email','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['id','sender','receiver','message']
    
    def validate(self,attrs):
        sender=attrs.get('sender')
        receiver=attrs.get('receiver')
        if sender==receiver:
            raise serializers.ValidationError("sender can't be receiver")
        check_sender = User.objects.get(id=sender.id)
        if not check_sender:
            raise serializers.ValidationError('sender does not exist')
        check_receiver = User.objects.get(id=receiver.id)
        if not check_receiver:
            raise serializers.ValidationError('receiver does not exist')
        return attrs

    