from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm
from django.contrib import messages
from django.http import HttpResponse

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success!')
            return HttpResponse('Registaration success!')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register_patient.html', {'form': form})


