from django.test import TestCase
import random
import string
from django.contrib.auth.models import User
from product.models import Product


 #Se crea caso de test para probar la creacion de unidades vendidas de PRODUCTOS

KEY_LEN = 5
char_list = [random.choice(string.digits) for _ in range(KEY_LEN)]
unvend = ''.join(char_list)
print(f'----------> PRODUCTOS: Resultado de TEST CASE: {unvend} Unidades vendidas')
        

product = Product(
code="code",
description="description",
unit_sales = unvend,
)

