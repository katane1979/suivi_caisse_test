from django.db import models

class Parametre(models.Model):
    solde_initial = models.DecimalField(
        "Solde initial de caisse", max_digits=15, decimal_places=2, default=0
    )
    annee_analyse = models.IntegerField("Année d'analyse", null=True, blank=True)

    def __str__(self):
        return f"Paramètres {self.annee_analyse or ''}"


class TypeMouvement(models.Model):
    libelle = models.CharField("Type de mouvement", max_length=50)

    def __str__(self):
        return self.libelle


class Caisse(models.Model):
    libelle = models.CharField("Caisse", max_length=50)

    def __str__(self):
        return self.libelle


class ModePaiement(models.Model):
    libelle = models.CharField("Mode de paiement", max_length=50)

    def __str__(self):
        return self.libelle


class MouvementCaisse(models.Model):
    date_mouvement = models.DateField("Date")
    num_piece = models.CharField("N° pièce", max_length=30, blank=True, null=True)
    libelle = models.CharField("Libellé / Description", max_length=150)

    type_mouvement = models.ForeignKey(
        TypeMouvement, on_delete=models.PROTECT, verbose_name="Type de mouvement"
    )
    caisse = models.ForeignKey(
        Caisse, on_delete=models.PROTECT, verbose_name="Caisse"
    )
    mode_paiement = models.ForeignKey(
        ModePaiement, on_delete=models.PROTECT, verbose_name="Mode de paiement"
    )

    entree = models.DecimalField(
        "Entrée (Crédit)", max_digits=15, decimal_places=2, blank=True, null=True
    )
    sortie = models.DecimalField(
        "Sortie (Débit)", max_digits=15, decimal_places=2, blank=True, null=True
    )

    observations = models.TextField("Observations", blank=True, null=True)
    piece_jointe = models.FileField(
        "Pièce jointe", upload_to="pieces/%Y/%m", blank=True, null=True
    )

    class Meta:
        ordering = ["date_mouvement", "id"]
        verbose_name = "Mouvement de caisse"
        verbose_name_plural = "Mouvements de caisse"

    def __str__(self):
        return f"{self.date_mouvement} — {self.libelle}"


