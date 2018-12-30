from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from domains.models import Domain
def service_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    instance = Service()
    return 'service_{0}/{1}'.format(instance.nom_service, filename)



class Service(models.Model):
    nom_service         = models.CharField(max_length=255, unique=True)
    slug_service        = models.SlugField(unique=True)
    description_service = models.TextField()
    image_service       = models.ImageField(upload_to=service_directory_path, null=True, blank=True)
    # domain_service      = models.ForeignKey(Domain, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom_service

    def __unicode__(self):
        return self.nom_service

def pre_save_service(sender, instance, *args, **kwargs):
    slug_service = slugify(instance.nom_service)
    instance.slug_service = slug_service

pre_save.connect(pre_save_service, sender=Service)
