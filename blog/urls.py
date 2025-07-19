from django.urls import path
from .views import BlogView, BlogDetail, BlogCreate,BlogUpdate,BlogDelete,ToggleLikeView

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('create/', BlogCreate.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='blog_delete'), 
     path('like/<int:pk>/', ToggleLikeView.as_view(), name='toggle_like'),
   
]