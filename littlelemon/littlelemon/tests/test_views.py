from django.tests import TestCase
from .models import Menu

class MenuViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Menu = Menu.objects.create(
            title='cheese',
            price=1.89,
            inventory=4,
        )

        def test_getall(self):
            self.assertIsInstance(self.Menu.title, str)
            self.assertIsInstance(self.Menu.price, str)
            self.assertIsInstance(self.Menu.inventory, str)