from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = ('title', 'body',)
    # change_list_template = 'admin/blog/blog_change_list.html'


admin.site.register(Post, PostAdmin)
