from django.db import models
from django.contrib.auth.models import User

# Example model for storing sector-related content
class SectorContent(models.Model):
    SECTOR_CHOICES = [
        ('IT', 'IT Sector'),
        ('ELE', 'Electrical & Electronic Sector'),
        ('PASSIVE', 'Passive Income Sector'),
    ]
    sector = models.CharField(max_length=20, choices=SECTOR_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.sector} - {self.title}"

