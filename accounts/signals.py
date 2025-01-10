from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from .models import Accounts

User = get_user_model()


@receiver(post_save, sender=User)
def create_main_account(sender, instance, created, **kwargs):
    if created:
        Accounts.objects.create(
            user = instance,
            currency = "NGN",
            balance = 0.00,
            interest_rate = 0.45,
            withdrawal_limit = 1000000.00,
            
        )