from rest_framework import serializers

from apps.watch.models import Watch, WatchCategory

class WatchCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchCategory
        fields = ('gender', 'style', 'condition')



class WatchSerializer(serializers.ModelSerializer):
    category = WatchCategorySerializer(read_only=True)
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'description', 'price', 'country', 'year', 'category')
