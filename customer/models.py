from django.db import models
import uuid

STATUS = {
    ('passport', 'Passport'),
    ('national_id', 'National ID'),
    ('driver_license', 'Driver License'),
}

class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True) 
    photo = models.ImageField()
    address = models.CharField(max_length=50, unique=True)  
    verification_status = models.CharField(max_length=40, choices=STATUS)
    id_number = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='kyc_documents/')
    verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Customer for {self.photo} ({self.id_number})" 
    
