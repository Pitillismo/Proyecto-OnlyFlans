from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flan
from .forms import ContactFormForm



# Create your views here. Se deberian hacer con clases y no funciones...

def index (request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'pages/index.html', {'flanes':flanes_publicos})

def about (request):
    return render(request, 'pages/about.html')

def exito(request):
    return render(request, 'pages/exito.html')

def welcome (request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'pages/welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST) #Validando lo que entre al contacto sea un post y no un get o put...
        if form.is_valid():
            form.save() #se guarda en el modelo y se va a la base de datos
            return redirect('exito') #redirecciona a la pagina exito       
    else:
        form = ContactFormForm()
    
    return render (request, 'pages/contacto.html', {'form': form})
