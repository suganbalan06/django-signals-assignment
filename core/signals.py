import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item

@receiver(post_save, sender=Item)
def my_signal(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(3)
    print("Signal finished")
