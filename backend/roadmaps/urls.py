from django.urls import path
from .views import *


urlpatterns = [
    path('create', RoadmapCreate.as_view(), name='create'),
    path('update/<int:pk>', RoadmapUpdate.as_view(), name='update'),
    path('create-roadmap-categ', RoadmapCategCreate.as_view(), name='create-roadmap-categ'),
    path('update-roadmap-categ/<int:pk>', RoadmapCategUpdate.as_view(), name='update-roadmap-categ'),
    path('create-roadmap-step', RoadmapStepCreate.as_view(), name='create-roadmap-step'),
    path('update-roadmap-step/<int:pk>', RoadmapStepUpdate.as_view(), name='update-roadmap-step'),
    path('create-roadmap-resource', ResourceCreate.as_view(), name='create-roadmap-resource'),
    path('update-roadmap-resource/<int:pk>', ResourceUpdate.as_view(), name='update-roadmap-resource'),
    path('<int:pk>', RoadmapRetrieve.as_view(), name='retrieve'),
]

