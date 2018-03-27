from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone, first_name,  password=None):
        """ Creates and saves a User with the given email and password."""

        if not phone:
            raise ValueError('Users must have a phone number')

        if not first_name:
            raise ValueError('Users must have a name')

        user = self.model(
            phone = phone,
            first_name = first_name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_staffuser(self, phone, first_name,  password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            phone = phone,
            first_name = first_name,
            password = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self, phone, first_name,  password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone = phone,
            first_name = first_name,
            password = password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(verbose_name="Мобильный номер", max_length=12, unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    verification_code = models.DecimalField(verbose_name="Код подтверждения номера",max_digits=4,decimal_places=0, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True)
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=255, blank=True)
    full_address = models.CharField(verbose_name="Адресс", max_length=255,blank=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name'] # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        if self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active