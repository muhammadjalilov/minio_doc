from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_files/')
    size = models.IntegerField()
    type = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.RESTRICT)

    def get_file_url(self):
        from .minio_runner import get_file_url
        return get_file_url(self.file)