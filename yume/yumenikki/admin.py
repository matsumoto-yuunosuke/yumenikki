from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import DreamModel, IdeaModel, DreamTag, User

# Register your models here.
class CutomUserAdmin(UserAdmin):
  fieldsets = (
    (None, {
      'fields': (
        'username',
        'password',
      )
    }),
    (None, {
      'fields': (
        'is_active',
        'is_admin',
      )
    })
  )

  list_display = ('username', 'is_active')
  list_filter = ()
  ordering = ()
  filter_horizontal = ()

class DreamTagInline(admin.TabularInline):
  model = DreamModel.dtags.through

class DreamModelAdmin(admin.ModelAdmin):
  inlines = [DreamTagInline]
  exclude = ['dtags']

admin.site.register(DreamModel, DreamModelAdmin)
admin.site.register(IdeaModel)
admin.site.register(DreamTag)
admin.site.unregister(Group)
admin.site.register(User, CutomUserAdmin)