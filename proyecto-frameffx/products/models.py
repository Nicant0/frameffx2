from django.db import models

class Producto(models.Model):

    TIPOS_PRODUCTO = [
        ("preset", "Preset"),
        ("guia", "Guía"),
        ("plugin", "Plugin"),
        ("proyecto", "Archivo de proyecto"),
        ("bundle", "Bundle"),
    ]

    titulo = models.CharField(
        max_length=150,
        verbose_name="Título"
    )
    descripcion = models.TextField(
        verbose_name="Descripción"
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_PRODUCTO,
        verbose_name="Tipo de producto"
    )
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Precio"
    )
    publicado = models.BooleanField(
        default=True,
        verbose_name="Publicado"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )

    def __str__(self):
        return self.titulo
