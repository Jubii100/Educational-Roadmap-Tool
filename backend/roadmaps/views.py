from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Prefetch
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class RoadmapCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoadmapCreateSerializer

    def create(self, request, *args, **kwargs):
        request.data["creator"] = request.user.id
        serializer = self.get_serializer(data=request.data)        
        # serializer.creator = request.user
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class RoadmapUpdate(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoadmapCreateSerializer

    def get_queryset(self):    
        queryset = Roadmap.objects.prefetch_related(
                                    Prefetch('steps',
                                            queryset=RoadmapStep.objects.prefetch_related(
                                                        Prefetch('resources',
                                                        queryset=Resource.objects.all())))
                                            ).all()
        return queryset   

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['pk'])
        obj = self.filter_queryset(obj)

        return obj

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


class RoadmapList(ListAPIView):
    serializer_class = RoadmapListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):    
        queryset = Roadmap.objects.all()
        return queryset  


class RoadmapDetail(RetrieveUpdateAPIView):
    serializer_class = RoadmapDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT']:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

    def get_queryset(self):    
        queryset = Roadmap.objects.prefetch_related(
                                    Prefetch('steps',
                                            queryset=RoadmapStep.objects.prefetch_related(
                                                        Prefetch('resources',
                                                        queryset=Resource.objects.all())))
                                            ).all()
        return queryset   
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['pk'])
        obj = self.filter_queryset(obj)

        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        roadmap_id = self.kwargs['pk']
        if request.data.get('steps'):
            request.data['steps'] = list(map(lambda d: {**d, 'roadmap': roadmap_id}, request.data['steps']))
        if request.data.get('steps', [{}])[0].get('resources'):
            request.data['steps'] = list(map(lambda d: {**d, 'resources': list(map(lambda d: {**d, 'step': RoadmapStep.objects.get(roadmap=roadmap_id, order=d['order'])}, d['resources']))}, request.data['steps']))
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        roadmap_id = self.kwargs['pk']
        if request.data.get('steps'):
            request.data['steps'] = list(map(lambda d: {**d, 'roadmap': roadmap_id}, request.data['steps']))
        if request.data.get('steps', [{}])[0].get('resources'):
            request.data['steps'] = list(map(lambda d: {**d, 'resources': list(map(lambda d: {**d, 'step': RoadmapStep.objects.get(roadmap=roadmap_id, order=d['order'])}, d['resources']))}, request.data['steps']))
        return self.partial_update(request, *args, **kwargs)    
    

class CreatorDetail(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH']:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

    def get_queryset(self):    
        queryset = User.objects.prefetch_related(
                                    Prefetch('roadmaps',
                                            queryset=Roadmap.objects.all())
                                            ).all()
        return queryset   
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['pk'])
        obj = self.filter_queryset(obj)

        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        creator_id = self.kwargs['pk']
        if request.data.get('roadmaps'):
            request.data['roadmaps'] = list(map(lambda d: {**d, 'creator': creator_id}, request.data['roadmaps']))

        return self.partial_update(request, *args, **kwargs) 