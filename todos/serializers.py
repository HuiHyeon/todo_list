from rest_framework import serializers
from .models import Todo, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('todo', 'id', 'contents', 'created_at', 'updated_at')


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    #comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description',
                  'is_completed', 'created_at', 'updated_at')
