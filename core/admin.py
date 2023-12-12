from django.contrib import admin

from core.models import Subscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'time', 'last_date_check')
