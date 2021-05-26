from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=20)

    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.slug

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

    #画像
    image_1 = models.ImageField(
        verbose_name = '画像1',
        upload_to='media/',
        blank=True, 
        null=True,
        )

    image_2 = models.ImageField(
        verbose_name = '画像2',
        upload_to='media/',
        blank=True,
        null=True,
        )

    image_3 = models.ImageField(
        verbose_name = '画像3',
        upload_to='media/',
        blank=True,
        null=True,
        )

    image_4 = models.ImageField(
        verbose_name = '画像4',
        upload_to='media/',
        blank=True,
        null=True,
        )

    create_time = models.DateField(
        verbose_name="投稿日",
        default=timezone.now
    )

    count = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} {self.content} \
        {self.image_1} {self.image_2} {self.image_3} {self.image_4} {self.create_time} {self.tags}"

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

    #画像
    image_1 = models.ImageField(
        verbose_name = '画像1',
        upload_to='media/',
        blank=True, 
        null=True,
        )

    image_2 = models.ImageField(
        verbose_name = '画像2',
        upload_to='media/',
        blank=True,
        null=True,
        )

    image_3 = models.ImageField(
        verbose_name = '画像3',
        upload_to='media/',
        blank=True,
        null=True,
        )

    image_4 = models.ImageField(
        verbose_name = '画像4',
        upload_to='media/',
        blank=True,
        null=True,
        )

    create_time = models.DateField(
        verbose_name="投稿日",
        default=timezone.now
    )

    def __str__(self):
        return f"{self.dream} {self.title} {self.content} \
        {self.image_1} {self.image_2} {self.image_3} {self.image_4} {self.create_time}"
