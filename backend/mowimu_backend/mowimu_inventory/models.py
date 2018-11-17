from django.db import models
   
class Place(models.Model):
    name = models.CharField(max_length = 1024)
    inside_place = models.ForeignKey('self', 
                                     null=True, 
                                     blank=True,
                                     related_name='contains_place', 
                                     on_delete=models.CASCADE)
    
    def __str__(self):
        if self.inside_place:
            return str(self.inside_place) + ' > ' + self.name
        else:
            return self.name

class Thing(models.Model):
    name = models.CharField(max_length = 1024)
    photo = models.ImageField(upload_to = 'thing_photos', default = 'thing_photos/nothing.png')
    location = models.ForeignKey(Place, 
                                 null=True, 
                                 blank=True,
                                 related_name='contains_thing',
                                 on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
