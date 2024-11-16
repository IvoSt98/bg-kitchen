from django.shortcuts import render
from  django.views.generic  import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'reastaurant/index.html'

class MakeReservation(TemplateView):
    template_name = 'reastaurant/make_reservation.html'

class ChangeReservation(TemplateView):
    template_name = 'reastaurant/change_reservation.html'

class ViewReservation(TemplateView):
    template_name = 'reastaurant/view_reservation.html'

