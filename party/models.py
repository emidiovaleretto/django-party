from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    '''
    Custom user model for the party app.
    '''


class Party(models.Model):
    '''
    Model representing a party event.
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation_note = models.TextField()
    venue = models.CharField(max_length=200)
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hosted_parties'
    )

    class Meta:
        '''
        Meta data for Party model.
        '''
        verbose_name_plural = "Parties"

    def __str__(self):
        return f"Party on {self.party_date} at {self.venue}"


class Gift(models.Model):
    '''
    Model representing a gift for a party.
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    gift = models.CharField(max_length=200)
    price = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.gift}"


class Guest(models.Model):
    '''
    Model representing a guest invited to a party.
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    is_attending = models.BooleanField(default=False)
    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"
