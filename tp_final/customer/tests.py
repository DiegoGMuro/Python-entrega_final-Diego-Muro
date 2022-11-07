import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from customer.models import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="User1",
            password="98746",
        )
        Customer.objects.create(name="Supermercado1", code=19, owner=self.test_user)
        Customer.objects.create(name="Supermercado2", code=15, owner=self.test_user)

        customer_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(customer_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(customer_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Customer.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_customer_model(self):
        """Customers creation are correctly identified"""
        Supermercado1_customer = Customer.objects.get(name="Supermercado1")
        Supermercado2_customer = Customer.objects.get(name="Supermercado2")
        self.assertEqual(Supermercado1_customer.owner.username, "User1")
        self.assertEqual(Supermercado2_customer.owner.username, "User1")
        self.assertEqual(Supermercado1_customer.code, 19)
        self.assertEqual(Supermercado2_customer.code, 15)

    def test_customer_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            customer_test = Customer.objects.get(name=mock_name)
            self.assertEqual(customer_test.owner.username, "User1")
            self.assertEqual(customer_test.code, mock_code)
