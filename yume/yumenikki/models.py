from django.db import models
from django.utils import timezone

# Create your models here.
class DreamModel(models.Model):
    class Meta:
        verbose_name = "あなたの夢"
        verbose_name_plural = 'あなたの夢'

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
    )
    content = models.TextField(
        verbose_name="内容"
    )

    image = models.ImageField(
        verbose_name="画像を投稿",
        blank=True
        )
    create_time = models.DateField(
        verbose_name="投稿日",
        default=timezone.now
    )

    def __str__(self):
        return self.title

class IdeaModel(models.Model):
    class Meta:
        verbose_name = "アイデア"
        verbose_name_plural = 'アイデア'
    
    dream = models.ForeignKey(
        DreamModel,
        verbose_name="Dream",
        on_delete=models.PROTECT
    )

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
    )
    content = models.TextField(
        verbose_name="内容"
    )

    image = models.ImageField(
        verbose_name="画像を投稿",
        blank=True
        )
    create_time = models.DateField(
        verbose_name="投稿日",
        default=timezone.now
    )

    def __str__(self):
        return self.title

# class DreamComment(models.Model):
#     text = models.TextField()
#     posted_at = models.DateTimeField(auto_now_add=True)
#     article = models.ForeignKey(to=DreamModel, related_name='comments', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.text