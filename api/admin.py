from django.contrib import admin

from api.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','modified')
    list_filter = ("status",)
    search_fields = ['title','body']

admin.site.register(Post,PostAdmin)