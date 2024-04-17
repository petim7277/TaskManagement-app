from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email"]
    list_per_page = 10
    list_filter = ["username", "email"]
    search_fields = ["username"]
    ordering = ["username"]


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_completed"]
    list_per_page = 10
    list_filter = ["title", "is_completed"]
    search_fields = ["title"]
    ordering = ["title"]
