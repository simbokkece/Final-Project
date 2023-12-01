"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# import class View
from .views import CustomLoginView, HomeView, CustomLogoutView, RegisterView, AdmissionView, GeneralView, AllergiesView, HistoryView, PatientView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admission/', AdmissionView.as_view(), name='admission'),
    path('general/', GeneralView.as_view(), name='general'),
    path('allergies/', AllergiesView.as_view(), name='allergies'),
    path('history/', HistoryView.as_view(), name='history'),
    path('patient/', PatientView.as_view(), name='patient')
]
