from django.shortcuts import render
from .forms import bookingForm

# Create your views here.


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_table.html', {'form': form})

def success(request):
    return render(request, 'bookings/success.html')