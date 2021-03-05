"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'