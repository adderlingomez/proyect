from django.shortcuts import render
#from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def contraseñas(request):
    characters = list('abcdeabcdefghijklmnopqrstuvwxyz')
    generador_contra  = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('especial'):
        characters.extend(list('#"%&=?¡@*¨[][_]'))  

    if request.GET.get('numeros'):
        characters.extend(list('0123456789'))  

    for x in range(length):
       generador_contra += random.choice(characters)

    return render(request, 'contraseña.html', {'contraseñas': generador_contra})

                                                         

