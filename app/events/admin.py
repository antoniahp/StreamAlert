from django.contrib import admin

from app.events.domain.event import Event

admin.site.register(Event)