from django import forms
from .models import bookings


class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['name', 'email', 'date', 'tiem', 'guests', 'special_requessts']