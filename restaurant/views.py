from django.shortcuts import render
from django.views.generic  import TemplateView, ListView
from .models import Reservations

# Create your views here.
class Index(TemplateView):
    template_name = 'restaurant/index.html'

class MakeReservation(TemplateView):
    template_name = 'restaurant/make_reservation.html'

class ChangeReservation(TemplateView):
    template_name = 'restaurant/change_reservation.html'

class ViewReservation(ListView):
    """
    1. Specify the model that this view will interact with
    2. The name of the template that will be used to render the view
    3. The context name for the reservations object, which will be used in the template
    """
    model = Reservations
    template_name = 'restaurant/view_reservation.html'
    context_object_name = 'reservations'
    
    """
    This method is used to decide what data (reservations) should be shown in the view.
    It returns all the reservations that belong to the logged-in user.
    """
    def get_queryset(self):
        return Reservations.objects.filter(user=self.request.user)