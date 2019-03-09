from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Artiste(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='artiste_punchline_image',null=True)

    def __str__(self):
        return self.nom

class Album(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
class Punchline(models.Model):
    punchline_contenu = models.CharField(max_length=250)
    poster_par = models.ForeignKey(User,on_delete = models.CASCADE)
    date_poste = models.DateTimeField(default=timezone.now)
    rappeur = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    rappeur_album = models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return self.punchline_contenu


class Comment(models.Model):
    punchline = models.ForeignKey(Punchline,on_delete=models.CASCADE,related_name='comments',null=True)
    #,null=True,blank=True
    auteur =models.CharField(max_length=200)
    text = models.TextField()
    date_comment = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
