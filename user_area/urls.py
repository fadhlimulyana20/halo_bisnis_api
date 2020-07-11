from .api import RegisterAPI, LoginAPI, UserAPI, UpdateEmailAPI, ChangePasswordAPI, ProfileAPI, UserProductAPI
from django.urls import path, include
from rest_framework import routers
from knox import views

router = routers.DefaultRouter()

urlpatterns = [
    path("/", include(router.urls)),
    path('auth', include('knox.urls')),
    path("auth/register", RegisterAPI.as_view()),
    path("auth/login", LoginAPI.as_view()),
    path("auth/myuser", UserAPI.as_view()),
    path("auth/email/update", UpdateEmailAPI.as_view()),
    path("auth/profile", ProfileAPI.as_view()),
    path("auth/change_password", ChangePasswordAPI.as_view()),
]

router.register('user_product', UserProductAPI, 'user_product')

urlpatterns += router.urls
