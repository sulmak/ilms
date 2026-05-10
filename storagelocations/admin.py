from django.contrib import admin
from .models import StorageLocation
# Register your models here.

class StorageLocationAdmin(admin.ModelAdmin):
  list_display = ("Code",  "UserName", "Sequence","Description", "Active", "AddedBy", "AddedDate")

admin.site.register(StorageLocation, StorageLocationAdmin)
