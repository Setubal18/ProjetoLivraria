from django.db import models


# Create your models here.

# autor = models.CharField(max_length=30)

class Editora(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=45)
    dataNascimento = models.DateField()
    dataMorte = models.DateField(null=True)

    verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=45)
    isbn = models.IntegerField()
    numero_paginas = models.IntegerField()
    anoPublicacao = models.DateField(unique_for_year='year')
    foto_capa = models.ImageField(upload_to='imagens')

    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, blank=False)
    autores = models.ManyToManyField(Autor)

    verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo
