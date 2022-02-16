from django.contrib import admin

from movie.models import Movie

# Register your models here.

from .models import Offer, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Movie, MovieAdmin)
