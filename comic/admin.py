from django.contrib import admin

from comic.models import Comic


class ComicAdmin(admin.ModelAdmin):
    list_display = ('name', 'types')
    search_fields = ('name',)


admin.site.register(Comic, ComicAdmin)
