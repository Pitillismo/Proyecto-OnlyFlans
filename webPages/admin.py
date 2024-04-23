from django.contrib import admin
from .models import Flan, ContactForm

class FlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_private']  # Muestra el precio en la lista
    fields = ['name', 'description', 'image_url', 'price', 'is_private', 'slug']  # Incluye el precio en el formulario de edición
# Registra el modelo Flan con la clase FlanAdmin
admin.site.register(Flan)

# Registra el modelo ContactForm de la forma usual
admin.site.register(ContactForm)

