from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
from shopInfo.models import ShopInformation

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message
        )
        contact.save()
        messages.success(request, 'Thank you for you contributing')

        return redirect('contact')
    else:
        shopInforQueryset = ShopInformation.objects.all()
        context = {
            'shopInformation': shopInforQueryset
        }
        return render(request, 'contacts/contact.html', context)