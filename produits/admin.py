from django.contrib import admin

# Register your models here.

from .models import Produit


admin.site.register(Produit)

@admin.register()
class Admin(admin.ModelAdmin):
    list_display = ("")


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    class Meta:
        model = Produit
        fields = '__all__'
