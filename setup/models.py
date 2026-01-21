from django.db import models

# Create your models here.
class Setup(models.Model):
    class Meta:
        managed = False
        permissions = [
            ('approve_setup', 'Can approve Setup section'),
        ]
        
    def __str__(self):
        return 'Setup'