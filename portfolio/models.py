from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
WEB = 'web'
DESKTOP = 'desktop'
DESIGN = 'design'
AUDIOVISUEL = 'audiov'
DEFAULT = ''

class Project(models.Model):
    DOMAINE_NAME = (
            (WEB, 'Web development'),
            (DESKTOP, 'Desktop Application'),
            (DESIGN, 'Design '),
            (AUDIOVISUEL, 'audiovisuel'),
            (DEFAULT, ''),
        )
    project_name = models.CharField(max_length=256)
    description = models.TextField()
    annee  = models.DateField(auto_now=False, auto_now_add=False)
    domaine = models.CharField(choices=DOMAINE_NAME,max_length=2,default=DEFAULT,)
    medayor_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
