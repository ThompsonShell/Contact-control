from django.db import models
from apps.users.models import CustomUser
from .tests.check_phone_number import is_valid_phone_number


class Contact(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='contacts',
        )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[is_valid_phone_number])
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.phone_number}"
    
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        unique_together = ('user', 'phone_number', 'name')
        

class Tag(models.Model):
    name = models.CharField(max_length=250, unique=True)
    contacts = models.ForeignKey('contacts.Contact', related_name='tags', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name    
    
