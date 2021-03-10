from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
import json
from shopInfo.models import ShopInformation

from .models import Appointment
from categories.models import Categories, Subcategories

def index(request):

    if request.method == 'POST':
        inputs = json.loads(request.POST.get('data'))["inputs"]
        selectedServices = json.loads(request.POST.get('data'))["selectedServices"]

        name = inputs['name']
        email = inputs['email']
        phone = inputs['phone']
        date = inputs['date']
        time = inputs['time']
        message = inputs['message']
        seletedServices = selectedServices

        appointment = Appointment(
            name = name,
            phone = phone,
            email = email,
            services = seletedServices,
            date = date,
            time = time,
            message = message
        )

        appointment.save()
        isNotAdded = appointment._state.adding 
        data = {
            'success': 'Thank you for booking with us.'
        }

        return JsonResponse(data)

    else:
        categoryArr = []
        categoriesQueryset = Categories.objects.all()
        shopInforQueryset = ShopInformation.objects.all()

        for category in categoriesQueryset:
            categoryArr.append(category.name)

        subCateArr = {}

        for name in categoryArr:
            subCateArr[name] = Subcategories.objects.all().filter(category__name=name)


        context = {
            "categories": categoriesQueryset,
            "subcategories": subCateArr,
            'shopInformation': shopInforQueryset
        }
        
        return render(request, 'appointments/appointment.html', context)