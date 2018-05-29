from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Month, Daily_info
from django.contrib.auth.models import User


def home(request):
    months = Month.objects.all()
    return render(request,  'home.html', {'months' : months})


def inside_month(request, pk):
    mon = get_object_or_404(Month, pk=pk)
    return render(request, 'inside_month.html', {'mon' : mon})


def new_entry(request, pk):
    mon = get_object_or_404(Month, pk=pk)

    if request.method == 'POST':
        date = request.POST['Date']
        income = request.POST['income']
        expense = request.POST['expense']
        description = request.POST['description']

        user = User.objects.first()

        day = Daily_info.objects.create(
            date = date,
            income = income,
            expenditure = expense,
            description = description,
            account = mon,
        )

        return redirect('inside_month', pk=mon.pk)

    return render(request, 'new_entry.html', {'mon': mon})
