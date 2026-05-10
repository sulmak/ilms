from django.contrib import admin
from .models import Rack

# Register your models here.

class RackAdmin(admin.ModelAdmin):
  list_display = ("Code",  "UserName", "Sequence", "Rows", "Columns","Description", "Active", "AddedBy", "AddedDate")

admin.site.register(Rack, RackAdmin)
