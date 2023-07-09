from rest_framework import serializers
from .models import *


class RoadmapCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapCateg
        fields = '__all__' 


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__' 


class RoadmapStepSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, required=False)
    class Meta:
        model = RoadmapStep
        fields = '__all__' 


class RoadmapSerializer(serializers.ModelSerializer):
    steps = RoadmapStepSerializer(many=True, required=False)
    class Meta:
        model = Roadmap
        fields = '__all__' 

