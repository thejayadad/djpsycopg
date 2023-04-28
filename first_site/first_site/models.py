

from django.db import models

class post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=300)

    class Meta:
        db_table: "post"

    
    def __str__(self):
        return self.title



