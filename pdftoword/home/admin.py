from django.contrib import admin
from . models import *
# Register your models here.
# admin.site.register(ConvertedFile)

class ConvertedFileAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        # Allow access only to admin users
        return request.user.is_superuser

admin.site.register(ConvertedFile, ConvertedFileAdmin)