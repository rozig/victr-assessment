from django.db import models


class Project(models.Model):
    repository_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    stars = models.IntegerField(null=False)
    url = models.URLField(null=False)
    created_date = models.DateTimeField(null=False)
    last_pushed_date = models.DateTimeField(null=False)
