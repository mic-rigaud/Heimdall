from django.db import models

# Create your models here.
class NetworkDatabase(models.Model):
    ip = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    time_last = models.CharField(max_length=100)
    confiance = models.CharField(max_length=100)
    statut = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0} [{1}] [{2}] [{3}] [{4}]".format( self.ip, self.mac, self.time_last, self.confiance, self.statut)
