from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import dataHMS


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        labels = {
            'username': _('Username'),
            'first_name': _('Nama Depan'),
            'last_name': _('Nama Belakang'),
            'email': _('Email')
        }

class DataPasien(forms.ModelForm):
    class Meta:
        model = dataHMS
        fields = "__all__"
        error_message = {
            'id': {
                'required': 'Anda harus mengisi form ID'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'tgl_lahir' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            },
            'height':{
                'required': "Anda harus mengisi form Tinggi Badan"
            },
            'weight':{
                'required': "Anda harus mengisi form Berat Badan"
            },
            'gender':{
                'required': "Anda harus mengisi form Jenis Kelamin"
            },
            'tgl_masuk':{
                'required': "Anda harus mengisi form Tanggal Masuk"
            },
            'diagnosis':{
                'required': "Anda harus mengisi form Diagnosis"
            },
            'bed':{
                'required': "Anda harus mengisi form Ranjang"
            }
        }