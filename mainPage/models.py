from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse
from Whym import settings
from django.db.models.signals import  pre_save
from django.utils.text import slugify
from django.utils import timezone

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return ' %s' % (self.name)

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return ' %s' % (self.name)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Status(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

class UserManager(BaseUserManager):
    def create_user(self, username, phone, password=None):
        """ Creates and saves a User with the given email and password."""

        if not username:
            raise ValueError('Users must have an unique name')
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            username=username,
            phone=phone,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_staffuser(self, username, phone,  password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self, username, phone,  password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="Имя пользователья", max_length=100,unique=True,)
    phone = models.CharField(verbose_name="Мобильный номер", max_length=12, unique=True)
    verification_code = models.DecimalField(verbose_name="Код подтверждения номера",max_digits=4,decimal_places=0, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True)
    birth_date = models.DateField(verbose_name="Дата рождения", null=True)
    email = models.EmailField(verbose_name='Email', max_length=255, blank=True)
    full_address = models.CharField(verbose_name="Адресс", max_length=255,blank=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone'] # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

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

class Message(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Кому", related_name="to_user")
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="От кого", related_name="from_user")
    text = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return '%s' % (self.text)

    class Meta:
        db_table = "message"
        verbose_name = "Message"
        verbose_name_plural = "Messages"

class PostManager(models.Manager):
    def active(self):
        return super(PostManager, self).filter(status=2).filter(updated_at__lte=timezone.now())

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, verbose_name="Автор", default=1)
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    slug = models.SlugField(unique = True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        verbose_name = "Фото",
        upload_to = upload_location,
        height_field = 'height_field',
        width_field = 'width_field',
        blank=True)
    height_field = models.IntegerField(verbose_name="Высота", default=0)
    width_field = models.IntegerField(verbose_name="Ширина", default=0)
    category = models.ForeignKey(Category,on_delete = models.CASCADE , verbose_name="Категория")
    city = models.ForeignKey(City,on_delete=models.SET_NULL, verbose_name="Город", null=True)
    status = models.ForeignKey(Status, default = 1, on_delete=models.CASCADE, verbose_name="Статус")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время обновления", auto_now=True)

    objects = PostManager()

    def __str__(self):
        return '%s' % (self.title)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.slug})

    class Meta:
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-updated_at']

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

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)