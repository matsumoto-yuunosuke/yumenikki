from django.contrib import admin
from yumenikki.models import DreamModel, IdeaModel, Tag

# Register your models here.
class TagInline(admin.TabularInline):
  model = DreamModel.tags.through

class DreamModelAdmin(admin.ModelAdmin):
  inlines = [TagInline]
  exclude = ['tags']

admin.site.register(DreamModel, DreamModelAdmin)
admin.site.register(IdeaModel)
admin.site.register(Tag)