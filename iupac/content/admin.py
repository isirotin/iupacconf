from models import *
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.register(Page)
admin.site.register(ImageFile)
admin.site.register(DocumentFile)
admin.site.register(DocumentFileType)
admin.site.register(Slide)


class HTMLContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HTMLContent
        fields = "__all__"


class HTMLContentAdmin(admin.ModelAdmin):
    form = HTMLContentAdminForm

admin.site.register(HTMLContent, HTMLContentAdmin)
admin.site.register(PlaintextContent)