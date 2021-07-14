from django.test import TestCase

from django.contrib.auth import get_user_model

class movies_crud_test(TestCase):

    def setUp(self):


        self.user = get_user_model().objects.create_user(
            username = 'Ahmed',
            email = 'ahmed.zatar2@gmail.com',
            password = '123456789a'
        )

    def test_create_new_user(self):

        self.assertEquals(self.user.email,'ahmed.zatar2@gmail.com')
        self.assertEquals(self.user.username,'Ahmed')
        

    def test_duplicate_emails(self):
        try:

            self.user2 = get_user_model().objects.create_user(
                username = 'Ahmed',
                email = 'ahmed.zatar2@gmail.com',
                password = '123456789a'
            )
            
        except:
            print('This email is used')

