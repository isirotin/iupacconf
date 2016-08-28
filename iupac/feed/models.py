from __future__ import unicode_literals

from django.db import models
from content.models import Page
from event.models import Event
from news.models import NewsItem
from django.utils import timezone
from taggit.managers import TaggableManager


class Deadline(models.Model):
    title = models.CharField(max_length=255)
    href = models.CharField(max_length=255, blank=True, null=True)
    page = models.ForeignKey(Page, blank=True, null=True)
    deadline = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title


class FeedItem(models.Model):
    news = models.ForeignKey(NewsItem, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    deadline = models.ForeignKey(Deadline, blank=True, null=True)
    title_override = models.CharField(max_length=255, blank=True, null=True)
    href_override = models.CharField(max_length=255, blank=True, null=True)
    show_datetime_override = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        if self.title_override:
            return self.title_override
        elif self.news:
            return self.news.title
        elif self.deadline:
            return self.deadline.title
        elif self.event:
            return self.event.title
        else:
            return str(self.date_create)