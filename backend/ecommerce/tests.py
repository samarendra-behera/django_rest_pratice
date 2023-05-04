from django.contrib.auth.models import User
from ecommerce.models import Item, Order
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class EcommerceTestCase(APITestCase):
    """
    Test suite for Items and Orders
    """

    def setUp(self):
        Item.objects.create(title= "Demo item 1",description= "This is a description for demo 1",price= 500,stock= 20)
        Item.objects.create(title= "Demo item 2",description= "This is a description for demo 2",price= 700,stock= 15)
        Item.objects.create(title= "Demo item 3",description= "This is a description for demo 3",price= 300,stock= 18)
        Item.objects.create(title= "Demo item 4",description= "This is a description for demo 4",price= 400,stock= 14)
        Item.objects.create(title= "Demo item 5",description= "This is a description for demo 5",price= 500,stock= 30)
        self.items = Item.objects.all()
        self.user = User.objects.create_user(
            username='epsumlabs',
            password='epsumlabs@123',
            email='epsumlabs@gmail.com'
        )
        Order.objects.create(item = Item.objects.first(), user=User.objects.first(), quantity=1)
        Order.objects.create(item = Item.objects.first(), user= User.objects.first(), quantity=2)

        # The app uses token authentication
        self.token = Token.objects.get(user= self.user)
        self.client = APIClient()

        # We pass the token in all calls to the API
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

    def test_get_all_items(self):
        '''
        test ItemViewSet list method
        '''
        self.assertEqual(self.items.count(), 5)
        response = self.client.get('/item/')
        self.assertEqual(response.status_code , status.HTTP_200_OK)
    def test_get_one_item(self):
        """
        test ItemViewSet retrive method
        """
        for item in self.items:
            response = self.client.get(f'/item/{item.id}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
