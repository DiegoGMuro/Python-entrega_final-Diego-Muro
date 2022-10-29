from django import forms


class ProductForm(forms.Form):
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