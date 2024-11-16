from django.urls import path
from . import views

"""
1.Home page: When the user visits the root URL
2. Booking page: When the user visits '/booking/',
the MakeReservation view is shown to allow
 making a new reservation.
3. View reservations: When the user visits '/view/',
the ViewReservation view is shown to display all 
the user's reservations.
4. Change reservation: When the user visits '/change/', 
the ChangeReservation view is shown to allow 
modifying an existing reservation.
"""
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('booking/', views.MakeReservation.as_view(), name='booking'),
    path('view/', views.ViewReservation.as_view(), name='view-reservation'),
    path('change/', views.ChangeReservation.as_view(), name='change-reservation'),
]