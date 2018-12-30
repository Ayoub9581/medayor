from django.db import models

# Create your models here.

class Domain(models.Model):
    nom_domaine = models.CharField(max_length=300)

    def __str__(self):
        return self.nom_domaine
    def __unicode__(self):
        return self.nom_domaine
