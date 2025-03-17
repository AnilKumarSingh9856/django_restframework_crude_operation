from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many = True, read_only = True)   # comments is related name that is given during model creation
    class Meta:
        model = Blog
        fields = ["id", "blog_title", "blog_body", "comments"]


