from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile, UserProduct
from product.models import Product

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        new_user.first_name = validated_data['first_name']
        new_user.last_name = validated_data['last_name']
        new_user.save()
        return new_user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    profile = ProfileSerializer()
    date_joined = serializers.DateTimeField(format="%d-%m-%Y")
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'profile')
    

class UpdateEmailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    profile = ProfileSerializer()
    date_joined = serializers.DateTimeField(format="%d-%m-%Y")
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        a = instance.check_password(validated_data.get('password'))
        print(a)
        if instance.check_password(validated_data.get('password')):
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance
        raise serializers.ValidationError()
        # else throw validation error

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to login with provided credentils")

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField()
    new_password = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)
    # updated_at = serializers.DateTimeField(format="%f")

    class Meta:
        model = Product
        fields = '__all__'


class UserProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = UserProduct
        fields = '__all__'