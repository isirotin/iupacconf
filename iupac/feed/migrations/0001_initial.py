# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('content', '0008_auto_20160828_1303'),
        ('event', '0002_auto_20160828_1315'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('href', models.CharField(blank=True, max_length=255, null=True)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Page')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_override', models.CharField(blank=True, max_length=255, null=True)),
                ('href_override', models.CharField(blank=True, max_length=255, null=True)),
                ('show_datetime_override', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('deadline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.Deadline')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.NewsItem')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
