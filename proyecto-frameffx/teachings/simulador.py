from faker import Faker
from .models import Teaching
import random

fake = Faker("es_ES")

def crearTeaching(n):
    for i in range(n):
        Teaching.objects.create(
            title_teaching=fake.name(), 
            estado=fake.name(),
            id_teaching=fake.random_int(),
            fecha_creacion=fake.date_time(),
            price_teaching=fake.pydecimal(left_digits=2, right_digits=2),
            end_at=fake.date_time(),                       
            start_at=fake.date_time(),
            duracion_min=fake.random_int(),
            description_teaching=fake.name(),
            )