from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Ride  # Assuming you have a Ride model
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to the dashboard or another page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import Ride  # Assuming you have a Ride model

def dashboard(request):
    if request.method == 'POST':
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time_str = request.POST.get('time')

        print(f"Received POST: pickup={pickup}, destination={destination}, date={date}, time={time_str}")  # Debug print

        if time_str:  # Check if time_str is provided
            try:
                time_obj = datetime.strptime(time_str, "%I:%M %p")
                formatted_time = time_obj.strftime("%H:%M")
                print(f"Formatted time: {formatted_time}")  # Debug print
            except ValueError:
                return render(request, 'home.html', {'error': 'Invalid time format. Please use HH:MM AM/PM.'})

            # Assuming you have a Ride model to store ride information
            ride = Ride(pickup=pickup, destination=destination, date=date, time=formatted_time, user=request.user)
            ride.save()
            print(f"Ride saved: {ride}")  # Debug print
            


            return HttpResponseRedirect(reverse('success'))  # Redirect to success page

        else:
            return render(request, 'home.html', {'error': 'Please select a time for your ride.'})
    return render(request, 'home.html')



    
def success_view(request):
    return render(request, 'success.html')  # Make sure to create success.html
