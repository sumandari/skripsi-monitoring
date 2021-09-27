from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass


@receiver(models.signals.post_save, sender=CustomUser)
def post_save_customuser_handler(sender, instance, created, **kwargs):
    """Add new user in mahasiswa group as default."""
    if created:
        group, group_created = Group.objects.get_or_create(name='mahasiswa')
        instance.groups.add(group)
        instance.save()