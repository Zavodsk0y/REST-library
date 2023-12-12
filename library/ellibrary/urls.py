from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='drf-auth'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)