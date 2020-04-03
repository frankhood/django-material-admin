from django.contrib.admin import ModelAdmin, register

from demo.relations.models import Relation


@register(Relation)
class RelationAdmin(ModelAdmin):
    list_display = ('id', 'name')
    icon_name = 'layers'
    autocomplete_fields = ('documents',)
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('user',)
