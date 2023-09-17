from rest_framework import serializers

from apps.watch.models import Watch, WatchCategory

class WatchCategorySerializer(serializers.ModelSerializer):
    diameter = serializers.SerializerMethodField()

    class Meta:
        model = WatchCategory
        fields = ('gender', 'style', 'condition', 'glass', 'case_material', 'dial_color', 'band_color',
                  'strap_material', 'case_shape', 'diameter', 'water_resistance', 'movement')

    def get_diameter(self, obj):
        return f"{obj.diameter} мм"


class WatchSerializer(serializers.ModelSerializer):
    category = WatchCategorySerializer(read_only=True)
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'description', 'price', 'country', 'year', 'category')
