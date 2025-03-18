from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')  # This will store the image in a folder called 'photos/'
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
