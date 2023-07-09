from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from django.contrib.auth.models import User
from .models import *
from .serializers import *

class RoadmapCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapSerializer

    # def get_queryset(self):    
    #     queryset = Roadmap.objects.prefetch_related(
    #                                 Prefetch('roadmapstep_set',
    #                                         queryset=RoadmapStep.objects.prefetch_related(
    #                                                     Prefetch('resource_set',
    #                                                     queryset=Resource.objects.all(),
    #                                                     to_attr='resources'),),
    #                                         to_attr='steps')
    #                                 ).all()
    #     return queryset

    def post(self, request, *args, **kwargs):
        creator_pk = User.objects.get(username = request.data.get('creator')).pk
        roadmap_categ_pk = RoadmapCateg.objects.get(name = request.data.get('category')).pk
        request.data['creator'] = creator_pk
        request.data['category'] = roadmap_categ_pk

        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class RoadmapUpdate(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapSerializer

    # def get_queryset(self):    
    #     queryset = Roadmap.objects.prefetch_related(
    #                                 Prefetch('roadmapstep_set',
    #                                         queryset=RoadmapStep.objects.prefetch_related(
    #                                                     Prefetch('resource_set',
    #                                                     queryset=Resource.objects.all(),
    #                                                     to_attr='resources'),),
    #                                         to_attr='steps')
    #                                 ).all()
    #     return queryset

    def post(self, request, *args, **kwargs):
        creator_pk = User.objects.get(username = request.data.get('creator')).pk
        roadmap_categ_pk = RoadmapCateg.objects.get(name = request.data.get('category')).pk
        request.data['creator'] = creator_pk
        request.data['category'] = roadmap_categ_pk
        
        return self.update(request, *args, **kwargs)


class RoadmapStepCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapStepSerializer

    def get_queryset(self):
        return RoadmapStep.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RoadmapStepUpdate(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapStepSerializer

    def get_queryset(self):
        return RoadmapStep.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class ResourceCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResourceSerializer

    def get_queryset(self):
        return Resource.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ResourceUpdate(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResourceSerializer

    def get_queryset(self):
        return Resource.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RoadmapCategCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapCategSerializer

    def get_queryset(self):
            
        return RoadmapCateg.objects.all()

    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
    

class RoadmapCategUpdate(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapCategSerializer

    def get_queryset(self):
            
        return RoadmapCateg.objects.all()

    def post(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)


class RoadmapRetrieve(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapSerializer


    def get_queryset(self):    
        queryset = Roadmap.objects.prefetch_related(
                                    Prefetch('roadmapstep_set',
                                            queryset=RoadmapStep.objects.prefetch_related(
                                                        Prefetch('resource_set',
                                                        queryset=Resource.objects.all(),
                                                        to_attr='resources'),),
                                            to_attr='steps')
                                    
                                    ).all()
        return queryset   
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['pk'])
        obj = self.filter_queryset(obj)

        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

