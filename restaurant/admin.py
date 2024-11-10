from django.contrib import admin
from .models import Reservations
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservations)
class ReservationsAdmin(SummernoteModelAdmin):
    list_display = ('user', 'people', 'date_and_time')
    search_fields = ['user']

# Register your models here.

