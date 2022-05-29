from django.shortcuts import render
from django import forms
from django.views.decorators.http import require_safe
from . models import Data


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


# @require_safe
def home(request): # NOSONAR
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SalaryForm()

    return render(request, 'home.html', {'form': form})
