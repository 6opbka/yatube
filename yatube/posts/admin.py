from django.contrib import admin

from .models import Post



class PostAdmin(admin.ModelAdmin):
    # Fields that should be shown in admin view
    list_display = ('text', 'pub_date', 'author')
    # Post search interface
    search_fields = ('text',)
    # Add the ability to filter by date
    list_filter = ('pub_date',)

admin.site.register(Post, PostAdmin)
# Register your models here.
