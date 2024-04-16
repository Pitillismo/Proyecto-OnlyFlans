from django.contrib import admin
from .models import Flan
from .models import ContactForm

# Register your models here.Se importa la clase y despes se tipea
admin.site.register(Flan)

admin.site.register(ContactForm)

