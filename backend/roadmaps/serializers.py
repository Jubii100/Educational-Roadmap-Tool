from rest_framework import serializers
from .models import *


class RoadmapCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapCateg
        fields = ['name']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class RoadmapStepSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, required=False)
    class Meta:
        model = RoadmapStep
        fields = '__all__' 


class RoadmapCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Roadmap
        fields = '__all__'


class RoadmapDetailSerializer(serializers.HyperlinkedModelSerializer):
    steps = RoadmapStepSerializer(many=True, required=False)
    creator = serializers.HyperlinkedRelatedField(view_name='creator-detail', lookup_field='pk',read_only=True)
    
    class Meta:
        model = Roadmap
        fields = ['url'] + [field.name for field in Roadmap._meta.fields] + ['steps']
        fields.remove('category')


class RoadmapListSerializer(serializers.ModelSerializer):
    creator = serializers.HyperlinkedRelatedField(view_name='creator-detail', lookup_field='pk',read_only=True)
    
    class Meta:
        model = Roadmap
        fields = ['url', 'title', 'creator', 'created_at', 'views_num', 'is_public']


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'