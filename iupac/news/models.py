from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
from content.models import HTMLContent
from django.utils import timezone
from event.models import Event


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(HTMLContent, blank=True, null=True)
    slug = models.SlugField()
    tags = TaggableManager()
    important = models.BooleanField(default=False)
    show_datetime = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    related_event = models.ForeignKey(Event, blank=True, null=True)

    def get_absolute_url(self):
        url = "/news/%s/" % self.slug
        return url

    def __unicode__(self):
        return self.title
