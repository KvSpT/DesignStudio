from django.contrib import admin
from .models import User, Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'designer', 'status', 'space_category', 'project_category')
    list_editable = ('status', 'space_category', 'project_category')
    list_filter = ('status', 'date_created')
    def has_add_permission(self, request):
        return False
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('initials', 'login', 'email')
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request):
        return False
