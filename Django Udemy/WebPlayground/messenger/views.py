from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread, Message
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

#Importando decorador para comprobar usuario registrado
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#Genera una respuesta json para la petición asíncrona
from django.http import JsonResponse

# Create your views here.

@method_decorator(login_required, name='dispatch')
# class ThreadList(ListView):
class ThreadList(TemplateView):
    # model = Thread
    
    # #Se deben devolver los hilos del usuario identificado

    # def get_queryset(self) -> QuerySet:
    #     return super(ThreadList, self).get_queryset().filter(users=self.request.user)

    template_name = 'messenger/thread_list.html'


@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    #Usuario solo pueda ver los hilos de los que forma parte
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()

        #Si el usuario no hace parte del hilo
        if self.request.user not in obj.users.all():
            raise Http404

        return obj

def add_message(request, pk):
    #print(request.GET)    
    json_response = {'created': False}

    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404('Usuario no identificado')

    return JsonResponse(json_response)


@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))