from django.shortcuts import render
from .models import Gallery
from shopInfo.models import ShopInformation

def index(request):
    queryset = Gallery.objects.all()
    shopInforQueryset = ShopInformation.objects.all()
    
    context = {
        'gallery': queryset,
        'shopInformation': shopInforQueryset
    }

    return render(request, 'gallery/gallery.html', context)