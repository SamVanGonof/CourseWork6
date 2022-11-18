from django.core.validators import MinLengthValidator
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название объявления')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads_images/', null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=1000, validators=[MinLengthValidator(1)])
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Автор")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
