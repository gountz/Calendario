from django.urls import path
from django.views.generic import TemplateView
from .views import CalendarioVista,CalendarioAnalisis,CalendarioAlgebra,CalendarioTaller, EditHour
app_name = 'Calendario'
urlpatterns = [
    path('',TemplateView.as_view(template_name="home.html"),name="home"),
    path('calendariovista',CalendarioVista.as_view(),name="calendariovista"),
    path('calendarioanalisis',CalendarioAnalisis.as_view(),name="calendarioanalisis"),
    path('calendarioalgebra',CalendarioAlgebra.as_view(),name="calendarioalgebra"),
    path('calendariotaller',CalendarioTaller.as_view(),name="calendariotaller"),
    path('<int:pk>/edithour',EditHour.as_view(),name="edit-hour"),
]