from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Devis(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    pays = CountryField()
    ville = models.CharField(max_length=200)
    commune = models.CharField(max_length=200)
    quartier = models.CharField(max_length=200)
    nom_client = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tel_whatsapp = PhoneNumberField()
    date = models.DateField(auto_now_add=True)
    numero_devis = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Devis"
        verbose_name_plural = "Devis"

    def __str__(self):
        return str(self.id)
