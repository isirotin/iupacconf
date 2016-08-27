from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
from filebrowser.base import FileObject


class HTMLContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=None)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class PlaintextContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=None)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=50)
    html_content = models.OneToOneField(HTMLContent, blank=True, null=True)
    plaintext_content = models.ForeignKey(PlaintextContent, blank=True, null=True)
    tags = TaggableManager()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class ImageFile(models.Model):
    alt = models.CharField(max_length=100)
    image_upload = models.ImageField(u"Image File", max_length=250, upload_to='uploads/', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tags = TaggableManager()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.alt


class DocumentFileType(models.Model):
    type = models.CharField(max_length=15)
    description = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ForeignKey(ImageFile, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.type


class DocumentFile(models.Model):
    alt = models.CharField(max_length=100)
    file_upload = models.FileField(u"File", max_length=250, upload_to='uploads/', blank=True, null=True)
    type = models.ForeignKey(DocumentFileType, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tags = TaggableManager()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.type


class Slide(models.Model):
    description = models.CharField(max_length=255)
    image = models.ForeignKey(ImageFile)

    def __unicode__(self):
        return self.description