from rest_framework.routers import DefaultRouter
from apps.watch.views import WatchViewSet, WatchCategoryViewSet

router = DefaultRouter()

router.register('watches', WatchViewSet)
router.register('watch_category', WatchCategoryViewSet)

urlpatterns = router.urls
