from ckeditor.widgets import CKEditorWidget
from django import forms

from credit.models import Credit

class CreditForm(forms.ModelForm):
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "credit-code",
                "placeholder": "Cód. del limite de credito",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripcion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "credit-description",
                "placeholder": "Desc. del limite credito",
                "required": "True",
            }
        ),
    )
    amount = forms.IntegerField(
        label="Monto maximo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "credit-amount",
                "placeholder": "Monto maximo permitido",
                "required": "True",
            }
        ),
    )    
    class Meta:
        model = Credit
        fields = ["code", "description", "amount"]       