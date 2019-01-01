from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from domains.models import Domain
from django.conf import settings
from django.urls import reverse


def service_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    instance = Service()
    return 'service_{0}/{1}'.format(instance.nom_service, filename)



class Service(models.Model):
    nom_service         = models.CharField(max_length=255, unique=True)
    slug        = models.SlugField(unique=True)
    description_service = models.TextField()
    image_service       = models.ImageField(upload_to=service_directory_path, null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    domain_service      = models.ForeignKey(Domain, on_delete=models.CASCADE)
    medayor_user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    timestamp =      models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.nom_service

    def __unicode__(self):
        return self.nom_service

    def timestamp_pretty(self):
        return self.timestamp.strftime("%x %X")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


def pre_save_service(sender, instance, *args, **kwargs):
    slug = slugify(instance.nom_service)
    instance.slug = slug

pre_save.connect(pre_save_service, sender=Service)
