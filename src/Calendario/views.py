from django.shortcuts import render, get_object_or_404
from .models import Calendario
from .forms import CalendarioForm
from django.views.generic import  ListView, UpdateView
# Create your views here.

class CalendarioVista(ListView):
    template_name = 'calendario.html'
    queryset = Calendario.objects.all()
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['LUNES'] = Calendario.objects.filter(dia="LUNES")
        context['MARTES'] = Calendario.objects.filter(dia="MARTES")
        context['MIERCOLES'] = Calendario.objects.filter(dia="MIERCOLES")
        context['JUEVES'] = Calendario.objects.filter(dia="JUEVES")
        context['VIERNES'] = Calendario.objects.filter(dia="VIERNES")
        context['SABADO'] = Calendario.objects.filter(dia="SÁBADO")
        context['DOMINGO'] = Calendario.objects.filter(dia="DOMINGO")
        return context
class CalendarioAnalisis(ListView):
    template_name = 'analisis.html'
    queryset = Calendario.objects.all()
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['LUNES'] = Calendario.objects.filter(dia="LUNES",description="ANALISIS")
        context['JUEVES'] = Calendario.objects.filter(dia="JUEVES",description="ANALISIS")
        context['ANALISIS'] = Calendario.objects.filter(description="ESTUDIAR ANALISIS")
        return context
class CalendarioAlgebra(ListView):
    template_name = 'algebra.html'
    queryset = Calendario.objects.all()
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['MARTES'] = Calendario.objects.filter(dia="MARTES",description="ALGEBRA")
        context['VIERNES'] = Calendario.objects.filter(dia="VIERNES",description="ALGEBRA")
        context['ALGEBRA'] = Calendario.objects.filter(description="ESTUDIAR ALGEBRA")
        return context
class CalendarioTaller(ListView):
    template_name = 'taller.html'
    queryset = Calendario.objects.all()
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['MIERCOLES'] = Calendario.objects.filter(dia="MIERCOLES",description="TALLER")
        context['TALLER'] = Calendario.objects.filter(description="ESTUDIAR TALLER")
        return context
class EditHour(UpdateView):
    template_name = 'edit_hour.html'
    form_class = CalendarioForm
    queryset = Calendario.objects.all()
    def get_object(self):
        id_=self.kwargs.get('pk')
        return get_object_or_404(Calendario, id=id_)
    def form_valid(self,form):
        return super().form_valid(form)