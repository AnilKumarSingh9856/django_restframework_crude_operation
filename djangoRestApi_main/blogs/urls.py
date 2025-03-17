from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.BlogsView.as_view(), name='blog_view'),
    path("comments/", views.CommentsView.as_view(), name='comments_view'),

    path('<int:pk>/', views.BlogViewDetails.as_view(), name='blog_details'),
    path('comments/<int:pk>/',views.CommentViewDetails.as_view(), name='comment_details'),

]