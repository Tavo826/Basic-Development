from django.db import models
from django.contrib.auth.models import User
#Importando una señal para comprobar a los usuarios en el thread
from django.db.models.signals import m2m_changed

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

#Model Manager
class ThreadManager(models.Manager):
    
    #Creando el filtro personalizado
    def find(self, user1, user2):
        #Dentro del método se hace referencia al propio queryset del modelo con self
        # self <=> Thread.objects.all()
        queryset = self.filter(users=user1).filter(users=user2)
        #Si se encuentra algo
        if len(queryset) > 0:
            return queryset[0]

        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        #Comprobando si el hilo existe
        if thread is None:
            #Creando el hilo
            thread = Thread.objects.create()
            #Añadiendo los usuarios
            thread.users.add(user1, user2)

        return thread


class Thread(models.Model):
    #el related_name permite hacer una búsqueda inversa de los mensajes que un usuario ha escrito con user.threads
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    #Para realizar la consulta, se filtra el queryset que devuelve Thread.objects

    #Gestor de modelos
    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']


def messages_changed(sender, **kwargs):
    #Recuperando la instancia (hilo)
    instance = kwargs.pop('instance', None)
    #Recuperando la acción
    action = kwargs.pop('action', None)
    #Recuperando conjunto de identificadores de los mensajes
    pk_set = kwargs.pop('pk_set', None)

    print(instance, action, pk_set)

    #Se pretende interceptar los mensajes del primary key (pk_set) y eliminar los mensajes
    #de los usuarios que no pertenecen a los usuarios en el hilo

    false_pk_set = set()

    #Interceptando los mensajes antes de que se añadan
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            #Autor del mensaje no es usuario del hilo
            if msg.user not in instance.users.all():
                print('--({}) no forma parte del hilo'.format(msg.user))
                #Se intercepta el mensaje fraudulento
                false_pk_set.add(msg_pk)

    #Se buscan los mensajes de false_pk_set que están en pk_set para eliminarlos
    pk_set.difference_update(false_pk_set)

    #Forzando la actualización del update
    instance.save()
    

#Conectando la señal con cualquier cambio que sucesa en el campo messages
m2m_changed.connect(messages_changed, sender=Thread.messages.through)
