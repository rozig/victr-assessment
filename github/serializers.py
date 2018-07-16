from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('repository_id', 'name', 'description', 'stars', 'url', 'created_date', 'last_pushed_date')
