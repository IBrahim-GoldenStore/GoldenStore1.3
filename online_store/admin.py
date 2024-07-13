from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display= ('name','price','quantity','category','top_category','description','image')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display= ('shopper_name','number','adresse','e_mail','name_and_quantity','montant','color')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display= ('name',)

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display= ('name','quantity','price',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name','image',)

@admin.register(Livraison)
class Livraison(admin.ModelAdmin):
    list_display= ('option',)