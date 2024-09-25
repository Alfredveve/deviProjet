from django.shortcuts import redirect, render
from .models import Devis, Service
from . forms import DevisForm, ServiceForm



def index(request):
    return render(request, 'app/index.html')


"""

def createDevis(request):
    form = DevisForm(request.POST or None, request.FILES)
    messages = ""
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = DevisForm()
        messages = 'Ajout bien passé'
    return render(request, 'app/createD.html', {'form': form, 'message': messages})
    


def createDevis(request):
    messages = ""
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            # Traitez les données valides du formulaire ici (par exemple, enregistrez-les dans la base de données)
            form.save()
            form = DevisForm()
            messages = "Devis bien soumit"
           
        else:
            # Gérez la soumission invalide du formulaire (par exemple, affichez les erreurs)
            messages = "Devis non soumit"
    else:
        form = DevisForm()

    
    return render(request, 'app/createD.html', {'form': form,'message': messages})
    
"""


# views.py
def createDevis(request):
    form = DevisForm(request.POST or None, request.FILES)
    messages = ""
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = DevisForm()
            messages = 'Ajout bien passé'
        else:
            messages = 'Erreur de validation du formulaire'
    return render(request, 'app/createD.html', {'form': form, 'message': messages})

    
def listD(request):
    devi = Devis.objects.all()
    context = {
        'devis': devi
    }
    return render(request, 'app/listDevis.html', context)



def createService(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    messages = ""
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ServiceForm()
        messages = "Ajout bien éffectué"
                
    return render(request, 'app/createS.html', {'form': form, 'message': messages})


# Ajout de la fonction qui permet d'afficher la liste des services

def listServices(request):
    service = Service.objects.all()
    
    context = {
        'services' : service
    }
    return render(request, 'app/listService.html', context)