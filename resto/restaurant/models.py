from django.db import models

# Create your models here.

class Plat(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=200)
    description = models.TextField()
    Price = models.DecimalField(decimal_places=2, max_digits=20)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of plat.
         """
         return reverse('plat-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.name