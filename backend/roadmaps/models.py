from django.db import models
from django.contrib.auth.models import User
from utilities.utils import validate_non_zero_oder

class RoadmapCateg(models.Model):
    name = models.CharField(unique=True, max_length=100, null=False)

    def __str__(self):
        return self.name


class Roadmap(models.Model):
    creator = models.ForeignKey(User, related_name='roadmaps', on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=200, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    category = models.ForeignKey(RoadmapCateg, on_delete=models.SET_NULL, null=True, blank=False)
    is_public = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    views_num = models.PositiveIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.title


class RoadmapStep(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    description = models.TextField(blank=True)
    roadmap = models.ForeignKey(Roadmap, related_name='steps', on_delete=models.CASCADE, null=False, blank=False)
    order = models.PositiveIntegerField(validators=[validate_non_zero_oder], null=False, blank=False)

    class Meta:
        unique_together = ('roadmap', 'order')
        
    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    step = models.ForeignKey(RoadmapStep, related_name='resources', on_delete=models.CASCADE, null=False, blank=False)
    is_online = models.BooleanField(default=True, null=False, blank=False)
    order = models.PositiveIntegerField(validators=[validate_non_zero_oder], null=False, blank=False)
    estimated_time = models.DurationField(null=False, blank=True)
    url = models.URLField(null=True)

    class Meta:
        unique_together = ('step', 'order')
        
    def __str__(self):
        return self.name
