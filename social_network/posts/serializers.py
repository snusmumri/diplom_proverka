from rest_framework import serializers

from posts.models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment_text', 'created_at',)
        #read_only_fields = ('user', )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'post_text', 'image', 'created_at', 'comments', 'likes_count')
        read_only_fields = ('user',)

    # def likes_count(self, posts):
    #     # likes_count = Like.objects.filter(post_id=posts.id).count()
    #     likes_count = Like.objects.count()
    #     return likes_count

