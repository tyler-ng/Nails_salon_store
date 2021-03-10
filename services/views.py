from django.shortcuts import render
from .models import Service
from categories.models import Categories, Subcategories
from shopInfo.models import ShopInformation

def get_nail_services(request):
    sub_categories = Subcategories.objects.filter(category__name__contains="Nails Services")
    shopInforQueryset = ShopInformation.objects.all()
    sub_cate_names = []
    sub_cate_photos = {}
    for obj in sub_categories:
        sub_cate_names.append(obj.name)
        sub_cate_photos[obj.name] = obj.photo
    
    service_objects = {}
    for name in sub_cate_names:
        service_object = Service.objects.filter(subcategory__name__contains=name)

        service_objects[name] = service_object
    
    context = {
        "services": service_objects,
        "sub_cate_photos": sub_cate_photos,
        'shopInformation': shopInforQueryset
    }
    return render(request, 'services/nails.html', context)

def get_tanning_services(request):
    sub_categories = Subcategories.objects.filter(category__name__contains="Tanning Services")
    shopInforQueryset = ShopInformation.objects.all()
    sub_cate_names = []
    sub_cate_photos = []
    for obj in sub_categories:
        sub_cate_names.append(obj.name)
        sub_cate_photos.append(obj.photo)
    
    service_objects = {}
    for name in sub_cate_names:
        service_object = Service.objects.filter(subcategory__name__contains=name)

        service_objects[name] = service_object

    first_service_objects = dict(list(service_objects.items())[:len(service_objects)//2])
    last_service_objects = dict(list(service_objects.items())[len(service_objects)//2:])
    print('sub_cate_photos: ', sub_cate_photos)
    print(last_service_objects)
    context = {
        "first_services": first_service_objects,
        "last_services": last_service_objects,
        "sub_cate_photos": sub_cate_photos,
        'shopInformation': shopInforQueryset
    }
    return render(request, 'services/tanning.html', context)