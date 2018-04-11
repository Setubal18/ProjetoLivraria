from django.contrib import admin
from .models import Autor,Editora,Livro
# Register your models here.
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Livro)