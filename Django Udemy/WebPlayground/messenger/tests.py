from django.test import TestCase
from django.contrib.auth.models import User
#importando los modelos
from .models import Message, Thread

# Create your tests here.


class ThreadTestCase(TestCase):
    #Preparando el entorno de pruebas
    def setUp(self):
        #Se crean 2 de usuarios
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')

        #Usuario de prueba
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        #Se crea un hilo para hacer pruebas
        self.thread = Thread.objects.create()

    #Creando el test (debe empezar con test_...)

    #Permite añadir usuarios
    def test_add_users_to_thread(self):
        #Añadiendo usuarios al hilo
        self.thread.users.add(self.user1, self.user2)
        #Comprobando que se añaden correctamente
        self.assertEqual(len(self.thread.users.all()), 2) #Comprobando que hay 2 usuarios

    #Permite recuperar un hilo existente a partir de sus usuarios
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        #Recuperando el hilo donde estén los 2 usuarios
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        #Comprobando
        self.assertEqual(self.thread, threads[0])

    #Permite comprobar que no existe un hilo cuando los usuarios no hacen parte de él
    def test_filter_non_existent_thread(self): #Debería devolver un queryset vacío (con 0 hilos)
        #Recuperando el hilo donde estén los 2 usuarios
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        #Comprobando
        self.assertEqual(len(threads), 0)

    #Permite generar mensajes de prueba
    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        #Creando los mensajes
        message1 = Message.objects.create(user=self.user1, content='Buenas las tenga')
        message2 = Message.objects.create(user=self.user2, content='Lo mismo digo')
        #Añadiendo los mensajes al hilo
        self.thread.messages.add(message1, message2)
        #Comparando que hayan 2 mensajes en el hilo
        self.assertEqual(len(self.thread.messages.all()), 2)

        #Mostrando los mensajes
        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))


    #Problema al ingresar un mensaje fraudulento
    def test_add_messages_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content='Buenas las tenga')
        message2 = Message.objects.create(user=self.user2, content='Lo mismo digo')
        #Mensaje de usuario que no pertenece al thread
        message3 = Message.objects.create(user=self.user3, content='Infiltrado')
        #Añadiendo los mensajes al hilo
        self.thread.messages.add(message1, message2, message3)
        #Deben ser 2 mensajes
        self.assertEqual(len(self.thread.messages.all()), 2) #Error 3!=2
        #Luego de modificar el modelo para eliminar el mensaje fraudulento, se valida el test

    
    #Test para el custom manager de find
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        #recuperando el hilo con un método propio (find)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)


    #Test para el custom manager de find_or_create
    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        #Si no existe el hilo, lo crea
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

        #Hilo que no existe
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread) #Comprueba si el hilo se creó

