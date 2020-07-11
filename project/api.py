from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import (
    ProjectSerializer,
    ProjectDetailSerializer,
)
from .models import (
    Project
)

class ProjectAPI(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self, *args, **kwargs):
        queryset = Project.objects.filter(user = self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailAPI(viewsets.ModelViewSet):
    serializer_class = ProjectDetailSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self, *args, **kwargs):
        queryset = Project.objects.filter(user = self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)