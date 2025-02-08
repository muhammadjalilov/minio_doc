from django.contrib import admin

from minio_doc.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'type', 'created_at', 'updated_at')
    search_fields = ('name', 'type')
    list_display_links = ('name',)
