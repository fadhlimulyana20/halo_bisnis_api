from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login
from django.contrib.auth.models import User

from knox.models import AuthToken

from .models import (
    Profile,
    UserProduct
)

from .serializers import (
    UserSerializer, 
    CreateUserSerializer, 
    LoginSerializer,
    UpdateEmailSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    UserProductSerializer
)

# User Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        update_last_login(None, user)
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })
    
    # def get_queryset(self):
    #     user = User
    #     return user.objects.all()

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        update_last_login(None, user)
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProfileAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user = self.request.user)

class UpdateEmailAPI(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UpdateEmailSerializer
    def get_object(self):
        return self.request.user


class ChangePasswordAPI(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
            
class UserProductAPI(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UserProductSerializer

    def get_queryset(self):
        return UserProduct.objects.filter(user = self.request.user)