from django.db import models


def user_directory_path(instance, filename):
    return 'movies/{0}/{1}'.format(instance.id, filename)
    
class Movie(models.Model):

    name = models.CharField(
        max_length=25, verbose_name='Название'
    )

    price = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Цена'
    )

    image = models.ImageField(
        verbose_name='Постер',
        upload_to = user_directory_path
    )

    def __str__(self):
        return "{}".format(self.name)
