from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from minio_doc.models import Document
from minio_doc.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(id=1))