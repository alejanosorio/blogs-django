from django.urls import path
from .views import BlogView, BlogDetail, BlogCreate,BlogUpdate,BlogDelete,ToggleLikeView
from. import views
urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('create/', BlogCreate.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='blog_delete'),
    path('like/<int:pk>/', ToggleLikeView.as_view(), name='toggle_like'),
    path('buscar/', views.blog_search, name='blog_search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


]