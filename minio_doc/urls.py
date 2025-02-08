from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from minio_doc.views import DocumentViewSet

router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = router.urls