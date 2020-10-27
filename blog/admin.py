from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date')
    list_display_links = ('id', 'author', 'title')
    list_filter = ('author',)
    search_fields = ('title', 'author')
    list_per_page = 10

admin.site.register(Post, PostAdmin)
