from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from services.models import Service
from domains.models import Domain

#
class Project(models.Model):
    project_name         = models.CharField(max_length=255)
    slug_project         = models.SlugField(unique=True)
    description          = models.TextField()
    annee                = models.DateField(auto_now=False, auto_now_add=False)
    domaine_project      = models.ForeignKey(Domain, on_delete=models.CASCADE)
    technologies_project = models.CharField(max_length=256)
    image_project = models.ImageField(upload_to='projects',null=True,blank=True)
    updated              = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp            = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=False)
    medayor_user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp','-updated']

    def __str__(self):
        return self.project_name

    def __unicode__(self):
        return self.project_name

def pre_save_project(sender, instance, *args, **kwargs):
    slug_project = slugify(instance.project_name)
    instance.slug_project = slug_project

pre_save.connect(pre_save_project, sender=Project)
