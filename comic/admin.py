from django.contrib import admin

from comic.models import Comic, DetailComic, TableChap, ViewComic


class ComicAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'types')
    search_fields = ('name',)


admin.site.register(Comic, ComicAdmin)
admin.site.register(DetailComic)
admin.site.register(TableChap)
admin.site.register(ViewComic)

