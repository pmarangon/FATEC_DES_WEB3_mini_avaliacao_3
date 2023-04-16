from django.contrib import admin
from holliday.models import Holliday

class HollidayAdmin(admin.ModelAdmin):
  list_display = ('nome','dia','mes')
  search_fields = ('dia',)

admin.site.register(Holliday, HollidayAdmin)
