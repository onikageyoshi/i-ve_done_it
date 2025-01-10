from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

DOCUMENT_TYPE_CHOICES = (
    ("NIN", "NIN"),
    ("Voter's Card", "Voter's Card"),
    ("Passport", "Passport"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=60, blank=True)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES, blank=True)
    front_cover = models.ImageField(upload_to="document_front_cover", blank=True)    
    back_cover = models.ImageField(upload_to="document_back_cover", blank=True)    

    def __str__(self) -> str:
        return f"{self.user} profile"


