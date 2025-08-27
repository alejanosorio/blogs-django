from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import BlogPost, Category
from .forms import BlogPostForm,CommentForm
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
class BlogView(LoginRequiredMixin,ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    paginate_by = 10
    login_url = '/login/'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        categoria = self.request.GET.get('categoria')

        if query:
            queryset = queryset.filter(title__icontains=query)
        if categoria:
            queryset = queryset.filter(category_id=categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        from .models import Category
        context['categorias'] = Category.objects.all()
        context['query'] = self.request.GET.get('q', '')
        context['selected_categoria'] = self.request.GET.get('categoria', '')
        return context

class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blogs'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user.username  # o email, etc.
            comment.save()
            return redirect('blog_detail', pk=self.object.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
    def get_category(self):
        return self.object.category

class BlogCreate(CreateView, LoginRequiredMixin):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('home')
    template_name = 'blog/blog_create.html'
    context_object_name = 'blogs'
    login_url = '/login/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class BlogUpdate(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('home')
    template_name = 'blog/blog_update.html'
    context_object_name = 'blogs'
    login_url = '/login/'
     def form_valid(self, form):
        # Si el usuario marcó "Eliminar imagen"
        if self.request.POST.get('image-clear'):
            if form.instance.image:
                form.instance.image.delete(save=False)  # borra el archivo físico
                form.instance.image = None  # borra la referencia en la BD
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('home')
    template_name = 'blog/blog_confirm.html'
    context_object_name = 'blogs'
    login_url = '/login/'
class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return redirect('blog_detail', pk=pk)

def blog_search(request):
       query = request.GET.get('q', '')  #
       results = BlogPost.objects.filter(title__icontains=query) if query else []
       return render(request, 'blog/search.html', {'results': results, 'query': query})


def about(request):
    return render(request, 'blog/about.html')
def contact(request):
    return render(request, 'blog/contact.html')
