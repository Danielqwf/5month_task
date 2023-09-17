from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from apps.watch.urls import router as watch_router


routers = [
    watch_router,
]

router = DefaultRouter()
for rtr in routers:
    router.registry.extend(rtr.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.watch.urls')),
    path('', include('apps.users.urls')),
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
