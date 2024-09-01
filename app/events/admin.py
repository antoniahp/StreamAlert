from django.contrib import admin

from events.domain.event import Event





class EventAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'category',
    ]

admin.site.register(Event, EventAdmin)