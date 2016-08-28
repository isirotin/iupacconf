from models import *
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


admin.site.register(ImageFile)
admin.site.register(DocumentFile)
admin.site.register(DocumentFileType)
admin.site.register(Slide)
admin.site.register(PlaintextContent)
admin.site.register(Banner)
admin.site.register(Topic)
admin.site.register(Person)
admin.site.register(PersonRole)

class HTMLContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HTMLContent
        fields = "__all__"


class HTMLContentAdmin(admin.ModelAdmin):
    form = HTMLContentAdminForm


admin.site.register(HTMLContent, HTMLContentAdmin)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)