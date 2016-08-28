from __future__ import unicode_literals
from django.db import models
from content.models import HTMLContent
from taggit.managers import TaggableManager
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(HTMLContent, blank=True, null=True)
    slug = models.SlugField()
    tags = TaggableManager()
    important = models.BooleanField(default=False)
    start_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        url = "/event/%s/" % self.slug
        return url

    def __unicode__(self):
        return self.title