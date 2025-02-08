from rest_framework import serializers

from minio_doc.minio_runner import upload_file, get_file_url
from minio_doc.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('name', 'file', 'size', 'type', 'content', 'created_at', 'updated_at', 'user')
        read_only_fields = ('created_at', 'updated_at','user', 'size', 'type')


    def create(self, validated_data):
        file = validated_data.pop('file')
        validated_data["size"] = file.size
        validated_data["type"] = str(file).split('.')[-1]
        file_url = upload_file(file, file.name)
        validated_data["file"] = file_url
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["file"] = str(instance.file)
        return data
