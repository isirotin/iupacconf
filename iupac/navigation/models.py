from __future__ import unicode_literals

from django.db import models
from content.models import Page


class MainMenuItem(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(Page, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    href = models.CharField(max_length=512, blank=True, null=True)
    blank = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if self.parent:
            return '%s -> %s' % (self.parent.title, self.title)
        else:
            return self.title


class BottomMenuItem(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(Page, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    href = models.CharField(max_length=512, blank=True, null=True)
    blank = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if self.parent:
            return '%s -> %s' % (self.parent.title, self.title)
        else:
            return self.title