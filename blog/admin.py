from django.contrib import admin
from blog.models import Article, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
class PostAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    #raw_id_fields = ("user",)
    search_fields = ['title',]
    #fields = ['title', 'user', ]
    inlines = [
        CommentInline,
    ]
admin.site.register(Article, PostAdmin)
