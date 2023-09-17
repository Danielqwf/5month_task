from django.contrib import admin

from apps.watch.models import Watch, WatchCategory


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'year')
    list_filter = ('brand', 'model', 'price', 'year')
    search_fields = ('brand', 'model', 'price', 'year')


@admin.register(WatchCategory)
class WatchCategoryAdmin(admin.ModelAdmin):
    list_display = ('condition', 'style', 'gender')
    list_filter = ('condition', 'style', 'gender')
    search_fields = ('watch__brand', 'watch__model')

