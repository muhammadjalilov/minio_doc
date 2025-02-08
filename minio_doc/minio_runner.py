from minio import Minio
from django.conf import settings

# Подключение к MinIO
minio_client = Minio(
    settings.MINIO_ENDPOINT.replace("http://", "").replace("https://", ""),
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False,  # Убираем SSL, если MinIO работает без HTTPS
)


# Загрузка файла
def upload_file(file, file_name):
    create_bucket()
    minio_client.put_object(
        settings.MINIO_BUCKET_NAME,
        file_name,
        file,
        length=-1,
        part_size=10 * 1024 * 1024,
    )
    return f"http://127.0.0.1:9001/browser/{settings.MINIO_BUCKET_NAME}/{file_name}"


# Создание бакета, если он не существует
def create_bucket():
    if not minio_client.bucket_exists(settings.MINIO_BUCKET_NAME):
        minio_client.make_bucket(settings.MINIO_BUCKET_NAME)


# Получение ссылки на файл
def get_file_url(file_name):
    return minio_client.presigned_get_object(settings.MINIO_BUCKET_NAME, file_name)
