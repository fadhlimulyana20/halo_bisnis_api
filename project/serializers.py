from rest_framework import serializers

from .models import (
    Project
)

from service.models import Technology 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class ProjectDetailSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer()

    class Meta:
        model = Project
        fields = '__all__'
    
    # def create(self, validated_data):
    #     name = validated_data['name']
    #     service = validated_data['service']
    #     technology = validated_data['technology']
    #     description = validated_data['description']
    #     # user = validated_data['user']
    #     design = validated_data['design']
    #     new_project = Project.objects.create(name = name, service = service, technology = technology, description = description, design = design)
    #     return new_project