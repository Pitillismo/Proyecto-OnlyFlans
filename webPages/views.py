from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Flan, Producto
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from webPages import models
from django.urls import reverse





# Create your views here. Se deberian hacer con clases (django funciona con clases, siempre con mayusculas) y no funciones...

def index (request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'pages/index.html', {'flanes':flanes_publicos})

def about (request):
    return render(request, 'pages/about.html')

def exito(request):
    return render(request, 'pages/exito.html')

@login_required #decorador para que solo se pueda acceder a la pagina si esta logueado
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

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Redirige a los usuarios ya autenticados que visitan la página de login

    def get_success_url(self):
        return reverse ('welcome')  # Redirecciona a la página de bienvenida tras el login exitoso

class CustomLogoutView(LogoutView):
    next_page = '/'

def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    
    # Si el flan es privado y el usuario no está autenticado, redirige al inicio de sesión.
    if flan.is_private and not request.user.is_authenticated:
        return redirect('login')
    # Si el flan no es privado o el usuario está autenticado, muestra los detalles.
    return render(request, 'pages/flan_detail.html', {'flan': flan})

def search_results(request):
    buscador = request.GET.get('buscador', '')
    print("Buscador:", buscador)  # Imprime el término de búsqueda recibido

    if buscador:
        if request.user.is_authenticated:
            # Todos los flanes si el usuario está autenticado
            flanes = Flan.objects.filter(Q(name__icontains=buscador))
        else:
            # Solo flanes públicos si el usuario no está autenticado
            flanes = Flan.objects.filter(Q(name__icontains=buscador), is_private=False)

        print("Flanes encontrados:", list(flanes))  # Imprime los flanes encontrados

        if not flanes:
            suggestions = Flan.objects.filter(is_private=False).order_by('?')[:5]
            print("Sugerencias:", list(suggestions))  # Imprime las sugerencias si no se encuentran flanes
        else:
            suggestions = []
    else:
        flanes = []
        suggestions = []

    context = {
        'flanes': flanes,
        'suggestions': suggestions
    }

    return render(request, 'pages/search_results.html', context)

