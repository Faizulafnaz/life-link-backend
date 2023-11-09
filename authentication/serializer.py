from .models import CustomUser
from rest_framework.serializers import ModelSerializer, ValidationError, ImageField
from rest_framework import serializers



class UserRegister(ModelSerializer):
 
    profile_picture = ImageField(read_only=True)
  
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'id', 'is_varified', 'otp', 'date_of_birth', 'profile_picture', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Email already exists.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
       
        password = validated_data.get('password')
        if password is None:
            validated_data.pop('password', None)

        return super().update(instance, validated_data)

class VarifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')

        try:
            user = CustomUser.objects.get(email=email)
       
            if user.otp != otp:
                raise serializers.ValidationError('Invalid OTP')

            # Update user verification status
            user.is_verified = True
            user.save()
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Invalid email')

        return data

    
