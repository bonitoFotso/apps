from distutils import text_file
from distutils.text_file import TextFile
from tabnanny import verbose
from django.db import models

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.DecimalField(max_digits=15000, decimal_places=2)

    class Meta:
        verbose_name =("Produit")
        verbose_name_plural = ("produits")
        
    def __str__(self):
        return self.nom
    
class categorie(models.Model):
    nom = models.CharField(max_length=50)
    
    class Meta:
        verbose_name =("categorie")
        verbose_name_plural = ("categories")
        
    def __str__(self):
        return self.nom
    
class telephone(models.Model):
    marque = models.CharField(max_length=50)
    modell = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    ram = models.DecimalField(max_digits=32,decimal_places=2)
    rom = models.DecimalField(max_digits=500,decimal_places=2)
    ecran = models.DecimalField(max_digits=32,decimal_places=2)
    poid = models.DecimalField(max_digits=32,decimal_places=2)
    dimention = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    detail = models.TextField()
    
    
class tv(models.Model):
    marque = models.CharField(max_length=50)
    modell = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    ecran = models.DecimalField(max_digits=32,decimal_places=2)
    poid = models.DecimalField(max_digits=32,decimal_places=2)
    dimention = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    detail = models.TextField()
    
genre ={
    "cle usb":"cle usb",
    "disque dur":"disque dur",
    "carte sd":"carte sd",
}
    
class stockage(models.Model):
    capaciter = models.DecimalField(max_digits=5, decimal_places=2)
    forme = models.CharField(max_length=50,)
    conectivite = models.CharField(max_length=50)
    vitesse = models.DecimalField(max_digits=5, decimal_places=1)
    nom = models.CharField(max_length=50)
    detail = models.TextField()