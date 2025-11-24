from django import forms
from django.utils import timezone

from .models import MouvementCaisse


class MouvementCaisseForm(forms.ModelForm):
    class Meta:
        model = MouvementCaisse
        fields = [
            "date_mouvement",
            "num_piece",
            "libelle",
            "type_mouvement",
            "caisse",
            "mode_paiement",
            "entree",
            "sortie",
            "observations",
            "piece_jointe",
        ]

        widgets = {
            "date_mouvement": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "num_piece": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Référence de la pièce (facultatif)",
                }
            ),
            "libelle": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Libellé du mouvement (obligatoire)",
                }
            ),
            "type_mouvement": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "caisse": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "mode_paiement": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "entree": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "Montant en entrée (crédit)",
                }
            ),
            "sortie": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "Montant en sortie (débit)",
                }
            ),
            "observations": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Observations éventuelles…",
                }
            ),
            "piece_jointe": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Date par défaut = aujourd'hui si non renseignée
        if not self.initial.get("date_mouvement"):
            self.fields["date_mouvement"].initial = timezone.now().date()

        # Ajout d’un petit * sur les champs obligatoires
        for name, field in self.fields.items():
            if field.required:
                field.label = f"{field.label} *"

    def clean(self):
        """
        Règle métier :
        - on ne peut PAS avoir une entrée ET une sortie
        - on doit avoir au moins l’un des deux
        """
        cleaned = super().clean()
        entree = cleaned.get("entree")
        sortie = cleaned.get("sortie")

        if entree and sortie:
            raise forms.ValidationError(
                "Vous ne pouvez pas saisir à la fois un montant en entrée ET en sortie pour le même mouvement."
            )

        if not entree and not sortie:
            raise forms.ValidationError(
                "Vous devez saisir soit un montant en entrée, soit un montant en sortie."
            )

        return cleaned
