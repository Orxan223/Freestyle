from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.

def gen_slug(s):
    return slugify(s,allow_unicode=False)

class Index(models.Model):
    title = models.CharField(max_length=127,blank=True,null=True)
    text = RichTextField()
    count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 50,blank=True,null=True)
    is_active = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:index_detail", kwargs={"slug": self.slug})
    
    
    
class Comment(models.Model):
    title = models.CharField(max_length=127)
    text = models.TextField(blank=True,null=True)
    index = models.ForeignKey(Index,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.title

   
@receiver(post_save, sender = Index)
def index_mail(sender, instance, created, **kwargs):
    if instance.is_active == True:
        message = " your post is activate"
        subject = "Updates"
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email,
            [instance.user.email,])

post_save.connect(index_mail, sender=Index)
