from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_view', 'status', 'published_at', 'created_at', 'updated_at',)
    list_filter = ('status', )
    ordering = ['-created_at']
    search_fields = ['title', 'content']
