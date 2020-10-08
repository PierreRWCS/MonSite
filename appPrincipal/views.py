from django.shortcuts import render
from django.http import HttpResponse

from appPrincipal.models import produits

def index(request):
    #obj = produits.objects.all()
    obj = produits.objects.filter(ingredients__name="boisson")
    sortie = []

    for i in obj:
        sortie.append(i.name + "||")

    return HttpResponse(sortie)

def desserts(request):
    #obj = produits.objects.all()
    obj = produits.objects.filter(ingredients__name="dessert")
    sortie = []

    for i in obj:
        sortie.append(i.name + "||")

    return HttpResponse(sortie)
# Create your views here.
