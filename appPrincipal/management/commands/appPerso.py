from django.core.management.base import BaseCommand, CommandError

from appPrincipal.models import ingredients, produits
import requests


class Command(BaseCommand):

    def __init__(self):
        self.mesCat = ["boisson", "dessert"]

    def recup_api(self):
        for cat in self.mesCat:
            cat_update = ingredients.objects.get_or_create(name=cat)
            cat_update[0].save()
            params_get = {
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "page_size": "1000",
                    "json": "1",
                    "tag_0":cat
                }
            data_raw = requests.get('http://fr.openfoodfacts.org/cgi/search.pl', params=params_get).json()
            for product in data_raw["products"]:
                try:
                    name = product["product_name_fr"]

                    prod = produits.objects.update_or_create(name=name, ingredients=cat_update[0])
                    prod[0].save()
                    
                except KeyError:
                    pass


    def handle(self, *arg, **options):
        self.recup_api()
        print(" ça marche!!!")
