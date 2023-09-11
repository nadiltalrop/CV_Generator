from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(blank=True,null=True)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(blank=True,null=True)
    skills = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name