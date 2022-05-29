from django.shortcuts import render
from django import forms
from .models import Data


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


def home(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SalaryForm()

    return render(request, 'home.html', {'form': form})
