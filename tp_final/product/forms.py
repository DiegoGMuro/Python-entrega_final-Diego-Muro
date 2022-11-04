from ckeditor.widgets import CKEditorWidget
from django import forms

from product.models import Product

class ProductForm(forms.ModelForm):
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "product-code",
                "placeholder": "Código del producto",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripcion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "product-description",
                "placeholder": "Descripcion del producto",
                "required": "True",
            }
        ),
    )
    unit_sales = forms.IntegerField(
        label="Unidades vendidas",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "product-unit_sales",
                "placeholder": "Unid. vendidas ult. mes",
                "required": "True",
            }
        ),
    )    
    class Meta:
        model = Product
        fields = ["code", "description", "unit_sales"]    