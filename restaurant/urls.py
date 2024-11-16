from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('booking/', views.MakeReservation.as_view(), name='booking'),
    path('view/', views.ViewReservation.as_view(), name='view'),
    path('change/', views.ChangeReservation.as_view(), name='change'),

]