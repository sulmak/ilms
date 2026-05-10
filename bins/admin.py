from django.contrib import admin
from .models import Bin

# Register your models here.
class BinAdmin(admin.ModelAdmin):
  list_display = ("Code",  "UserName", "Sequence", "Rows", "Columns", "AddedBy", "AddedDate")

admin.site.register(Bin, BinAdmin)
