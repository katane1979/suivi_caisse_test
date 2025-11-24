from django.contrib import admin
from .models import (
    Parametre,
    TypeMouvement,
    Caisse,
    ModePaiement,
    MouvementCaisse,
)

admin.site.register(Parametre)
admin.site.register(TypeMouvement)
admin.site.register(Caisse)
admin.site.register(ModePaiement)
admin.site.register(MouvementCaisse)



