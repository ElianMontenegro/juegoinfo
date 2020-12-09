from django.db import models


class JuegoManager(models.Manager):
    """ managers de productos """
    #def para filtrar los jurgos
    def search_juego(self, kword):  
        if len(kword) < 0:
            return Juego.objects.all
        else:
            return self.filter(
                name__icontains=kword
            )

