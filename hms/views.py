from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, DataPasien
from .models import dataHMS

class CustomLoginView(LoginView):
	template_name = 'accounts/login.html';
	redirect_authenticated_user = True


class HomeView(View):
    template_name = 'accounts/home.html'

    def get(self, request):
        return render(request, self.template_name)


class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = 'login'


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})


class AdmissionView(View):
    def get(self, request):
        form = DataPasien(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect("/")
            pass
        return render(request,"admission.html",{'form': form})

class PatientView(View):
    def get(self, request):
        hasil = dataHMS.objects.all()
        print(hasil)
        data = {
            'data' : hasil,
        }   
        return render(request, "data_pasien.html", data)  