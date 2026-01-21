from django.db import models

# Create your models here.
class Hub(models.Model):
    class Meta:
        managed = False
        permissions = [
            ('approve_hub', 'Can approve Hub section'),
        ]
        
    def __str__(self):
        return 'Hub'