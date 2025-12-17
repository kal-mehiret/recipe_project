from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Recipe

@receiver(pre_save, sender=Recipe)
def check_title(sender, instance, **kwargs):
    # Example: Ensure title is capitalized
    if instance.title:
        instance.title = instance.title.title()