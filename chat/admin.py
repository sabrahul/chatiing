from django.contrib import admin
from .models import Message,User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','is_staff','is_superuser']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver','message','created_at']



