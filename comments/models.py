from django.db import models
from Whym import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type    = ContentType.objects.get_for_model(instance.__class__)
        object_id       = instance.id
        qs              = super(CommentManager, self).filter(content_type=content_type, object_id=object_id).filter(parent=None)
        return qs

class Comment(models.Model):
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')
    text            = models.TextField(verbose_name="Комментарий")
    created_at      = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    parent          = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    objects         = CommentManager()

    def __str__(self):
        return '%s' % (self.author.get_full_name())

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    class Meta:
        db_table            = "comment"
        verbose_name        = "comment"
        verbose_name_plural = "comments"
        ordering = ["-created_at"]