from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(self, username, email, password, is_staff, is_superuser, address, **extra_fields):
    now = timezone.now()
    if not username:
      raise ValueError(('The given username must be set'))
    email = self.normalize_email(email)
    user = self.model(username=username, email=email,
             is_staff=is_staff, is_active=True,
             is_superuser=is_superuser, last_login=now,
             date_joined=now, address=address, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, username, email=None, password=None, **extra_fields):
    return self._create_user(username, email, password, False, False, True,
                 **extra_fields)

  def create_superuser(self, username, email, password, **extra_fields):
    user=self._create_user(username, email, password, True, True,
                 **extra_fields)
    user.is_active=True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250, blank= False)
    last_name = models.CharField(max_length=250, blank= False)
    email = models.EmailField(('email address'), unique = True)
    username = models.CharField(max_length=50, unique=True, blank=False, default='username')
    image = models.ImageField(blank=True)
    address = models.CharField(('address'), max_length=30, blank=True, null=True)
    Job_title = models.CharField(max_length=10)
    Cv = models.FileField()
    Experience = models.CharField(max_length=250, blank=True)
    nationality = models.CharField(max_length=250, blank=False, null=False)
    birth_date = models.DateField(('birth date'), auto_now=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USER_TYPES = (
    ('Job Seeker', 'Job Seeker'),
    ('Employer', 'Employer'),
    )
    user_type = models.CharField(('user type'), choices=USER_TYPES, max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


