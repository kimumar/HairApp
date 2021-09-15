from django.contrib import admin
from . models import BookingMessage, CommentMessage, Post, Setting
# Register your models here.
class BookingMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class CommentMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

    


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')

class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(BookingMessage, BookingMessageAdmin)
admin.site.register(CommentMessage, CommentMessageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Setting, SettingAdmin)