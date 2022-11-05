from ckeditor.widgets import CKEditorWidget
from django import forms

from payment.models import Payment

class PaymentForm(forms.ModelForm):
    code = forms.IntegerField(
        label="Codigo",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "payment-code",
                "placeholder": "Condicion de pago",
                "required": "True",
            }
        ),
    )
    name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "payment-name",
                "placeholder": "Desc. condicion de pago",
                "required": "True",
            }
        ),
    )
    days = forms.IntegerField(
        label="Dias",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "payment-days",
                "placeholder": "Dias max. permitidos",
                "required": "True",
            }
        ),
    )    
    class Meta:
        model = Payment
        fields = ["code", "name", "days"]    