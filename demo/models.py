from django.db import models

# Create your models here.
class Demo(models.Model):
    class Meta:
        managed = False
        permissions = [
            ('approve_demo', 'Can approve Demo section'),
        ]
        
    def __str__(self):
        return 'Demo'