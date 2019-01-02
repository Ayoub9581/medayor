from django.db import models
from django.db.models.signals import pre_save, post_save


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    note = models.TextField()
    adresse_ip = models.CharField(max_length=255,null=True,blank=True)
    host_contact = models.CharField(max_length=255,null=True,blank=True)
    server_name_contact = models.CharField(max_length=255,null=True,blank=True)
    http_user_agent = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

# def pre_save_adresse_ip(sender,instance,*args,**kwargs):
#     adresse_ip =
