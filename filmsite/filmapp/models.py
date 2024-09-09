from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    TCAT=(('Movie','Movie'),('Web-Series','Web-Series'),('Drama','Drama'))
    LCAT=(('English','English'),('Hindi','Hindi'),('Marathi','Marathi'))
    CCAT=(('India','India'),('America','America'),('Korea','Korea'))

    name=models.CharField(max_length=50,verbose_name='Film Name')
    is_paid=models.BooleanField(default=False)
    price=models.FloatField(default=0)
    type=models.CharField(verbose_name='Type',choices=TCAT,max_length=100)
    language=models.CharField(verbose_name='Language',choices=LCAT,max_length=100)
    country=models.CharField(verbose_name='Country',choices=CCAT,max_length=100)
    time=models.CharField(verbose_name='Time',max_length=100)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='image')
    video=models.FileField(upload_to='videos/', null=True, verbose_name='video')
    views=models.BigIntegerField(verbose_name='views',default=0)

    def __str__(self):
        return self.name + ": " + str(self.video)
        #return self.name 

    #def __str__(self):
        #return self.name

    
class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    fid=models.ForeignKey('Film',on_delete=models.CASCADE,db_column='fid')

class Plans(models.Model):
    name=models.CharField(max_length=20,verbose_name='name')
    duration=models.CharField(max_length=50,verbose_name='duration')
    charges=models.IntegerField(verbose_name='charges')

'''class Subscriptions(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Plans',on_delete=models.CASCADE,db_column='pid')'''

'''class History(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    fid=models.ForeignKey('Film',on_delete=models.CASCADE,db_column='fid')'''


class FilmHistory(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    fid=models.ForeignKey('Film',on_delete=models.CASCADE,db_column='fid')

class Watchlist(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    fid=models.ForeignKey('Film',on_delete=models.CASCADE,db_column='fid') 

class Subscribers(models.Model):
    pid=models.ForeignKey('Plans',on_delete=models.CASCADE,db_column='pid')
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')