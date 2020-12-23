from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class  userprofileinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #additionl
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    


from django.db import models

# Create your models here.
class Task(models.Model):
    #title=models.TextField()
    title=RichTextUploadingField(blank=True,null=True,)
    heading=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Task1(models.Model):
    title=RichTextUploadingField(blank=True,null=True,)
    #title=models.TextField()
    heading=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class names(models.Model):
    title=models.CharField(max_length=100)
    #title=models.TextField()

    def __str__(self):
        return self.title
