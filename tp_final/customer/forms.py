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
        max_length=40,
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
        label="Segmento (Agregar Regiones)",
        required=False,
        widget=CKEditorWidget(),        
    )
    image = forms.ImageField()
    
    class Meta:
        model = Customer
        fields = ["code", "name", "email", "segment", "image"]
        
class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )        