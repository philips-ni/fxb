from django.db import models
from django.conf import settings
from .services import SuperHeroWebAPI
import datetime


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Basic'),
        (1, 'Founder'),
        (2, 'Investor'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    user_type = models.IntegerField(null=True,
                                    choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}: {:.20}". format(self.user, self.bio or "")

    @property
    def get_age(self):
        today = datetime.date.today()
        return (today.year - self.birthdate.year) - int(
            (today.month, today.day) <
            (self.birthdate.month, self.birthdate.day))

    class Meta:
        abstract = True


class FounderProfile(models.Model):
     product_founded = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class InvestorProfile(models.Model):
    product_invested = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class Profile(InvestorProfile, FounderProfile, BaseProfile):
    pass
