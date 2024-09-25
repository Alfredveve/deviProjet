from django.contrib import admin
from . models import Devis, Service


class DevisAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'pays', 'ville', 'commune', 'quartier', 'nom_client', 'email', 'tel_whatsapp', 'numero_devis']

admin.site.register(Devis, DevisAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'description', 'prix_unitaire']

admin.site.register(Service, ServiceAdmin)
