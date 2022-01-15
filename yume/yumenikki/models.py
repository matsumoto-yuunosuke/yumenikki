from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username address')
        user = self.model(
            username = self.model.normalize_username(username)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

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

class DreamTag(models.Model):
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
        unique=True
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

    dtags = models.ManyToManyField(DreamTag, blank=True)

    def __str__(self):
        return self.title



# class IdeaTag(models.Model):
#     slug = models.CharField(primary_key=True, unique=True, max_length=20)

#     name = models.CharField(unique=True, max_length=20)

#     def __str__(self):
#         return self.slug

class IdeaModel(models.Model):
    class Meta:
        verbose_name = "アイデア"
        verbose_name_plural = 'アイデア'


    # """views.py idea_id
    # pk == id
    # # 指定したアイデアに紐づいたドリームモデルのid or titleを取得
    # # idだった場合はこれで処理は終了
    # idea_id = IdeaModel.objects.filter(id=idea_id).dream
    # # IdeaModel.objects.filter(id=idea_id) -> 指定したアイデアに紐づいたドリームモデルを取得 -> <QuerySet: [(dream: ~), (title: ~), (content: ~)... ...]>
    # # IdeaModel.objects.filter(id=idea_id).dream -> 上の中からdreamのみ取得 -> idかtitileかわからない？

    # # idの場合はそれをreturnで返すだけ。

    # # titleのばあい...
    # idea_id = DreamModel.objects.get(title=idea_title).id -> ドリームモデルのタイトルの中から先ほど取得したタイトルが一致するデータを取得して、そのidを取得

    # # idea_title = IdeaModel.objects.get(id=idea_id).title   # IdeaModelからtitleを取得したい場合...
    # return redirect ~

    # """
    
    dream = models.ForeignKey(
        DreamModel,
        verbose_name="Dream",
        on_delete=models.PROTECT,
    )

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
        unique=True
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
        
# カレンダーモデル       
class Booking(models.Model):
    member = models.ForeignKey(DreamModel, verbose_name='テスト夢', on_delete=models.CASCADE)
    nick_name = models.CharField('ニックネーム', max_length=100, null=True, blank=True)
    place = models.TextField('招待url', default='')
    start = models.DateTimeField('開始時間', default=timezone.now)
    end = models.DateTimeField('終了時間', default=timezone.now)
    
    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')
        
        return f'{self.nick_name} {start} ~ {end}'