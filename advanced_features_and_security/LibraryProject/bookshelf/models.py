from .models import Post
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superuser must have is_staff=True.'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser
    """
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Custom permissions defined in the Post model for detailed access control

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         permissions = [
#             ("can_view", "Can view post"),
#             ("can_create", "Can create post"),
#             ("can_edit", "Can edit post"),
#             ("can_delete", "Can delete post"),
#         ]

#     def __str__(self):
#         return self.title


def setup_groups():
    post_content_type = ContentType.objects.get_for_model(Post)

    # Define permissions
    permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            permission = Permission.objects.get(
                codename=perm, content_type=post_content_type)
            group.permissions.add(permission)


setup_groups()
