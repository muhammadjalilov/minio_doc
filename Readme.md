# Minio Django REST API

## Overview
This project is a Django REST framework application that integrates with MinIO for object storage. The application uses `django-storages` to handle file uploads to MinIO.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Docker & Docker Compose
- Python 3.8+
- pip

### Clone the Repository
```sh
git clone https://github.com/muhammadjalilov/minio_doc.git
cd minio_doc
```

### Environment Variables
Create a `.env` file in the project root and configure the necessary environment variables:
```env
MINIO_ENDPOINT="http://minio:9000"
MINIO_ACCESS_KEY=minio
MINIO_SECRET_KEY=minio123
MINIO_BUCKET_NAME="documents"
MINIO_ROOT_USER=minio
MINIO_ROOT_PASSWORD=minio123
```

### Build and Start the Project
```sh
docker-compose up -d --build
```

### Apply Migrations and Create a Superuser
```sh
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py createsuperuser
```

### Access the Application
- Django API: [http://localhost:8000](http://localhost:8000)
- MinIO Web UI: [http://localhost:9001](http://localhost:9001) (Login with `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY`)

## Usage
- Upload files via the Django API, and they will be stored in MinIO.
- Manage files via the MinIO Web UI.

Using MinIO Client (mc)

MinIO provides a command-line tool (mc) for managing storage.
To configure it, run:

```sh
mc alias set myminio http://localhost:9000 minio minio123
```

To list available buckets:

```sh
mc ls myminio
```

To upload a file:
```sh
mc cp myfile.txt myminio/documents/
```

Usage

Upload files via the Django API, and they will be stored in MinIO.

Manage files via the MinIO Web UI or mc client.

## Stopping the Project
To stop the containers, run:
```sh
docker-compose down
```

## License
This project is without a license.

