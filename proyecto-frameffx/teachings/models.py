from django.db import models

class Teaching(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Título"
    )
    description = models.TextField(
        verbose_name="Descripción"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio"
    )
    start_at = models.DateTimeField(
        verbose_name="Fecha y hora de inicio"
    )
    end_at = models.DateTimeField(
        verbose_name="Fecha y hora de fin"
    )
    duracion_min = models.PositiveIntegerField(
        verbose_name="Duración (minutos)"
    )

    ESTADOS = [
        ("activa", "Activa"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="activa",
        verbose_name="Estado"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )

    def __str__(self):
        return self.title
