from django.db import models
from django.contrib.auth.models import User

from contacts_manager.models import Contact


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True, null=True, related_name='profile')

    def __str__(self):
        return f"Profile: {self.first_name} {self.last_name}"
