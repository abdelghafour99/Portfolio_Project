from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
from .form import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'The Account of {username}! was created Successsfuly')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request,'register.html', {'form':form})