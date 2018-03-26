from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

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