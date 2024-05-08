from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField()
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        likes_count = Like.objects.count()
        # likes_count = Like.objects.filter(id=Post.id).count()
        return likes_count


    def __str__(self):
        return self.post_text

# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    like = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Ok'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  #, null=True, blank=True)

    def __str__(self):
        return self.comment_text