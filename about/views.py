from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import About
from shopInfo.models import ShopInformation

def index(request):
    try:
        queryset = About.objects.all()[0]
        shopInforQueryset = ShopInformation.objects.all()
    except:
        queryset = None
        shopInforQueryset = None
    context = {
        'about': queryset,
        'shopInformation': shopInforQueryset
    }

    return render(request, 'about/about.html', context)
