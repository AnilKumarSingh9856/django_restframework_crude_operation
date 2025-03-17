from django.shortcuts import render
from rest_framework import generics
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializers, CommentSerializers
from rest_framework.filters import SearchFilter, OrderingFilter



# Create your views here.
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']  # if we put '^' symbol in fron of this parameter then it filter data i.e the starting point of whole data not single word
    ordering_fields = ['id']

class BlogViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'pk'


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

class CommentViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = 'pk'