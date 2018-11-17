from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length = 1024)
    photo = models.ImageField(upload_to = 'thing_photos', default = 'thing_photos/nothing.png')
    