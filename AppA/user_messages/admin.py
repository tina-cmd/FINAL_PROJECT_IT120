from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'encrypted_content']
 
# Register the Message model so it appears in the Django admin
admin.site.register(Message, MessageAdmin)
