from django.db import models
from django.urls import reverse
# Create your models here.
DIAS = (
    ('LUNES',('LUNES')),
    ('MARTES',('MARTES')),
    ('MIERCOLES',('MIERCOLES')),
    ('JUEVES',('JUEVES')),
    ('VIERNES',('VIERNES')),
    ('SÁBADO',('SÁBADO')),
    ('DOMINGO',('DOMINGO')),
)
HOUR = (
    ('00:00',('00:00')),
    ('01:00',('01:00')),
    ('02:00',('02:00')),
    ('03:00',('03:00')),
    ('04:00',('04:00')),
    ('05:00',('05:00')),
    ('06:00',('06:00')),
    ('07:00',('07:00')),
    ('08:00',('08:00')),
    ('09:00',('09:00')),
    ('10:00',('10:00')),
    ('11:00',('11:00')),
    ('12:00',('12:00')),
    ('13:00',('13:00')),
    ('14:00',('14:00')),
    ('15:00',('15:00')),
    ('16:00',('16:00')),
    ('17:00',('17:00')),
    ('18:00',('18:00')),
    ('19:00',('19:00')),
    ('20:00',('20:00')),
    ('21:00',('21:00')),
    ('22:00',('22:00')),
    ('23:00',('23:00')),
)
class Calendario(models.Model):
    dia = models.CharField(choices=DIAS, max_length=10)
    hour = models.CharField(choices=HOUR, max_length=6)
    description = models.TextField(max_length=100, blank=True)
    def __str__(self):
        return f'Fecha:{self.dia}-Hora:{self.hour}'
    def get_absolute_url(self):
        return reverse('Calendario:calendariovista')
    class Meta:
        ordering = ['hour']
    