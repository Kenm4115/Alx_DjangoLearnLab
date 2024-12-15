
from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content',
                  'author_username', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author',
                  'content', 'created_at', 'updated_at']
