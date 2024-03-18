from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserTestCase(TestCase) :
    def test_create_user(self) :
        email = 'oz@oz.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self) :
        email = 'oz_super@oz.com'
        password = 'password'

        super_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)

        