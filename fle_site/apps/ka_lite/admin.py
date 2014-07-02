from django.contrib import admin
from django.contrib.auth.models import User

from models import UserResource


class UserResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "version")}
    list_display = ('title', 'version', 'doc_id', 'filename')

admin.site.register(UserResource, UserResourceAdmin)

