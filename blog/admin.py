from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
  search_fields = ['title']
  list_display = ['title']
  prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
  search_fields = ['title', 'description', 'body']
  list_display = ['title', 'category', 'posted_at']
  prepopulated_fields = {'slug': ['title']}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)