import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from payment.models import Payment

 #Se crea caso de test para probar la creacion Dias de CONDICION DE PAGO

KEY_LEN = 3
char_list = [random.choice(string.digits) for _ in range(KEY_LEN)]
diasp = ''.join(char_list)
print(f'----------> CONDICION DE PAGO: Resultado de TEST CASE: {diasp} dias de Condicion de pago creado')
        

payment = Payment(
code = "code",
name="name",
days=diasp,
)