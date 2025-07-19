# forms.py
from django import forms
from .models import BlogPost,Category,CommentPost

class BlogPostForm(forms.ModelForm):
      
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category', 'tags', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['title'].label = "Blog Title"
        self.fields['content'].label = "Content"
        self.fields['image'].label = "Upload Image (optional)"
        self.fields['category'].label = "Category"
        self.fields['tags'].label = "Tags (optional)"
        self.fields['is_published'].label = "Publish this blog"

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            tags_list = [tag.strip() for tag in tags.split(',')]
            return ', '.join(tags_list)
        return ''

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        return content

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and not image.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            raise forms.ValidationError("Image must be a PNG, JPG, JPEG, or GIF file.")
        return image

    def save(self, commit=True):
        blog_post = super(BlogPostForm, self).save(commit=False)
        if commit:
            blog_post.save()
        return blog_post    
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dejá tu comentario...'})
        } 