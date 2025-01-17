from django.contrib import admin

from .models import TelegramProfile, UserProfile


@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "telegram_id")  # Fields to display in the list view
    search_fields = ("user__username", "telegram_id")  # Enable search by username and telegram_id
    list_filter = ("user",)  # Filter by user
    raw_id_fields = ("user",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name")  # Fields to display in the list view
    search_fields = ("user__username", "user__phone_number")  # Enable search by username and telegram_id
    list_filter = ("user",)  # Filter by user
    raw_id_fields = ("user",)
