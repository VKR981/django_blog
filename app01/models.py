from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=50)
    _from = models.CharField(max_length=30)
    slug = AutoSlugField(max_length=80, unique=True,
                         populate_from=['title', '_from'])
    timestamp = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(default='')
    link = models.URLField()
    datetime = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, to_field='username', unique=False)


class Comment(models.Model):

    comment = models.CharField(max_length=140)
    username = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, to_field='username', unique=False)
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, to_field='slug', unique=False)
    datetime = models.DateTimeField(auto_now=True)
