from django.contrib import admin

# admin name = recxo , pass = 0987

# Register your models here.
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
