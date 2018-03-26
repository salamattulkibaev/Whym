from django.db import models
from Whym import settings
from posts.models import Post

class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    # Может быть поле to_comment

    def __str__(self):
        return '%s' % (self.text)

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"