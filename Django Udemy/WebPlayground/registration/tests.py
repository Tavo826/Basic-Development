from django.test import TestCase
#Se cargan los modelos
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    #Se reescribe el método setUp para preparar la prueba
    def setUp(self):
        #Se crea un usuario de prueba, permite pasarle una contraseña que se encripta automáticamente
        User.objects.create_user('test', 'test@test.com', 'test1234')

    #Se crea el método para la prueba (debe empezar por test_)
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        #Ejecutando el TestCase
        self.assertEqual(exists, True)