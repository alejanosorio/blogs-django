from django.contrib import admin
from .models import BlogPost, Category, CommentPost,Like

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'publish_date', 'views',  'likes_count','comments_count')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('is_published', 'category', 'publish_date')
    prepopulated_fields = {'tags': ('title',)}
    ordering = ('-publish_date',)
    def likes_count(self, obj):
        return obj.like.count()
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author', 'content')
    ordering = ('-created_at',)     


    
   
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_filter = ('post', 'user')
    search_fields = ('user',)