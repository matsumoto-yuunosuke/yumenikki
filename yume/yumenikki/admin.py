from django.contrib import admin
from .models import DreamModel, IdeaModel, DreamTag

# Register your models here.
class DreamTagInline(admin.TabularInline):
  model = DreamModel.dtags.through

class DreamModelAdmin(admin.ModelAdmin):
  inlines = [DreamTagInline]
  exclude = ['dtags']

admin.site.register(DreamModel, DreamModelAdmin)
admin.site.register(IdeaModel)
admin.site.register(DreamTag)