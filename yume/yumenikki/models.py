from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


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

    def __str__(self):
        return f"{self.title} {self.content} \
        {self.image_1} {self.image_2} {self.image_3} {self.image_4} {self.create_time}"

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
