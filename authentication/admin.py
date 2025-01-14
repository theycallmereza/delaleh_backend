from django.contrib import admin

from authentication.models import Consumer


@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ("name", "api_key")
    readonly_fields = ("api_key",)
