from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .paginations import StandardResultsSetPagination
from .models import Watch, WatchCategory
from .serializers import WatchSerializer, WatchCategorySerializer

class WatchViewSet(ModelViewSet):
    queryset = Watch.objects.all().prefetch_related('category').order_by('id')
    serializer_class = WatchSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['brand', 'model']


class WatchCategoryViewSet(ModelViewSet):
    queryset = WatchCategory.objects.all()
    serializer_class = WatchCategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
