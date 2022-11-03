from ckeditor.widgets import CKEditorWidget
from django import forms

from customer.models import Customer

class CustomerForm(forms.ModelForm):
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-code",
                "placeholder": "Código del cliente",
                "required": "True",
            }
        ),
    )          
    name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-name",
                "placeholder": "Nombre del cliente",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "customer-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    segment = forms.CharField(
        label="Segmento",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "customer-segment",
                "placeholder": "segmento del cliente",
                "required": "True",
            }
        ),
    )
 
    class Meta:
        model = Customer
        fields = ["code", "name", "email", "segment"]