from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.core.validators import RegexValidator
# from django.contrib.gis.utils import GeoIP

USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'



class MyUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('user must have an email')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username,email,password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser):
    email       = models.EmailField(verbose_name="Email", max_length=255)
    username    = models.CharField(max_length=255, validators=[RegexValidator(
                    regex = USERNAME_REGEX,
                    message='Username must be alphanumeric',
                    code='invalude Username'
                    )] , unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the suer have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

def profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_{0}/{1}'.format(instance.user.id, filename)





class TeamManager(models.Manager):
    def team(self, *args, **kwargs):
        return super(TeamManager, self).filter(is_team=True)

class Team(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    firsname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    team_user_image = models.ImageField(upload_to=profile_directory_path,null=True,blank=True)
    mission = models.CharField(max_length=255)
    is_team = models.BooleanField(default=False)

    def __str__(self):
        return self.mission

    @property
    def full_name(self):
        first = self.firsname + " " +  self.lastname
        return first

    objects = TeamManager()


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Team.objects.created(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
