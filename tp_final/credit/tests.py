from django.test import TestCase
import random
import string
from django.contrib.auth.models import User
from credit.models import Credit



 #Se crea caso de test para probar la creacion de montos de LIMITE DE CREDITO

KEY_LEN = 8
char_list = [random.choice(string.digits) for _ in range(KEY_LEN)]
montolim = ''.join(char_list)
print(f'----------> LIMITE DE CREDITO: Resultado de TEST CASE: {montolim} Es el monto maximo que se otorga a un cliente')
        

credit = Credit(
code="code",
description="description",
amount = montolim,
)
