from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

# Model Region
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

# Model City
class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return ' %s %s %s' % (self.id, self.name, self.region)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

# Model Category
class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Model Status
class Status(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

class UserManager(BaseUserManager):

    def create_user(self, username, phone , password=None, is_active = True, is_staff = False, is_admin = False):
        """
        Creates and saves a User with the given username, phone and password.
        """
        if not username:
            raise ValueError('Users must have the username')

        if not phone:
            raise ValueError('Users must have a phone number')

        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            username = username,
            phone = phone,
        )

        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self, username, phone, password):
        """
        Creates and saves a staff user with the given username, phone and password.
        """
        user = self.create_user(
            username,
            phone,
            password = password,
            is_staff=True,
        )
        return user

    def create_superuser(self, username, phone, password):
        """
        Creates and saves a superuser the given username, phone and password.
        """
        user = self.create_user(
            username,
            phone,
            password = password,
            is_staff=True,
            is_admin=True,
        )
        return user


# class User(models.Model) :
class User(AbstractBaseUser):

    username = models.CharField(verbose_name="Username", max_length=100,unique=True)
    phone = models.CharField(verbose_name="Мобильный номер", max_length=12,unique=True)
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

    def __str__(self):  # __unicode__ on Python 2
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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active