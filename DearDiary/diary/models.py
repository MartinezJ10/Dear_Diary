from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class DiaryPage(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    date_page = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(null=True)
    MOOD = (
        ("Delighted", "Delighted"),
        ("Excited", "Excited"),
        ("Neutral", "Neutral"),
        ("Speechless", "Speechless"),
        ("Happy", "Happy"),
        ("Flirty", "Flirty"),
        ("Sad", "Sad"),
        ("Guilty", "Guilty"),
        ("Broken", "Broken"),
        ("Shitty", "Shitty"),
        ("Furious", "Furious"),
        ("Nervous", "Nervous"),
    )
    mood = models.CharField(max_length=50, null=True, choices=MOOD)

    def __str__(self):
        return self.title
