from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    # description = models.TextField()
    completed = models.BooleanField(default=False)
    # upload = models.ImageField(upload_to='uploads/')
    upload = ImageField(upload_to='blog/uploads',
                        blank=True, null=True, default='')

    def _str_(self):
        return self.title
