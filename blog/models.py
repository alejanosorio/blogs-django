from django.db import models
from django.contrib.auth.models import User
 

choices = [('Tech', 'Tech'),
           ('Lifestyle', 'Lifestyle'),
           ('Travel', 'Travel'),
           ('Sport', 'Sport'),
           ('Finance', 'Finance'),
           ('Entertainment', 'Entertainment')]
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='blog_posts', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    views = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class CommentPost(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} '
class Like(models.Model):
    post = models.ForeignKey(BlogPost, related_name='like', on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')
   

    def __str__(self):
        return f'Like by {self.user} on {self.post.title}'