from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=250)
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
    def save_tag(self):
        self.save()


class Card(models.Model):
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    note = models.TextField(max_length=30000)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def save_article(self):
        self.save()

    def delete_card(self):
        self.delete()
    
    def update_card(self):
        pass


