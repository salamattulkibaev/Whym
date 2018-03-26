from django.db import models
from Whym import settings

class Recall(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Напишите отзыв")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return '%s' % (self.text)

    class Meta:
        db_table = "recall"
        verbose_name = "Recall"
        verbose_name_plural = "Recalls"