from django.test import TestCase, Client
from django.urls import reverse
from Authenticate.forms import CreateNewUser


class TestingForm(TestCase):
    
    def setUp(self) -> None:

        self.cliente = Client()
        self.url = reverse("register")

        self.data = {

            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300Ua",
            "password2": "3144300Ua"
        }

        self.data_two = {

            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300U",
            "password1": "31443U"
        }

        self.send = {

            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300UA",
            "password1": "3144300UA"
        }

        self.new_password = {
            "old_password": "3144300Ua",
            "new_password1": "3017454086Ua",
            "new_password2": "3017454086Ua"
        }

        #test with all the correct fields
        self.form = CreateNewUser(data=self.data)

        #test with all the incorrect fields
        self.form_two = CreateNewUser(data=self.data_two)


    def test_is_valid_form(self):
        self.assertTrue(self.form.is_valid(), msg="returns True if all the fields are correct")


    def test_is_not_valid_form(self):
        self.assertFalse(self.form_two.is_valid(), msg="returns False if all the fields are correct")


    def test_form_send_data_ok(self):
        response = self.client.post(self.url, self.send)
        self.assertEquals(response.status_code, 200, msg="returns a 200 status code when the user send the data")
