from django.contrib import admin
from .models import BorrowRecord, Member, MemberProfile 
# Register your models here.
admin.site.register(BorrowRecord)

admin.site.register(Member)
admin.site.register(MemberProfile)