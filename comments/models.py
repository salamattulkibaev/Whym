from django.db import models
from Whym import settings
from posts.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    # to_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Объявление")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)


    def __str__(self):
        return '%s' % (self.author.get_full_name())

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"