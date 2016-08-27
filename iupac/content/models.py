from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


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
    slug = models.SlugField()
    html_content = models.OneToOneField(HTMLContent, blank=True, null=True)
    plaintext_content = models.ForeignKey(PlaintextContent, blank=True, null=True)
    tags = TaggableManager()
    parent = models.ForeignKey('self', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        url = "/%s/" % self.slug
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.slug,url)
            page = page.parent
        return url


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


class IconLink(models.Model):
    ICONLINK_CHOICES = (
        ('Organizator', 'Organized by'),
        ('Collaborator', 'In collaboration with'),
        ('Cooperator', 'In cooperation with'),
        ('Accomodation', 'Accommodation and Travel by'),
        ('Supporter', 'Main supporters:'),
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    href = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ICONLINK_CHOICES, default=None, blank=True, null = True)

    def __unicode__(self):
        return self.title