from django.shortcuts import render
from .models import BannerSlider, WhyChooseUs, ServiceImage, Testimonials, SpecialPrice
from shopInfo.models import ShopInformation
from categories.models import Categories, Subcategories


def index(request):
    bannerSliderQueryset = BannerSlider.objects.all()
    whyChooseUsQueryset = WhyChooseUs.objects.all()
    serviceImageQueryset = ServiceImage.objects.all()
    testimonialQueryset = Testimonials.objects.all()
    specialPriceQueryset = SpecialPrice.objects.all()
    shopInforQueryset = ShopInformation.objects.all()
    categoriesQueryset = Categories.objects.all()
    # subCategories = Subcategories.objects.all()
    categoryArr = []
    for category in categoriesQueryset:
        categoryArr.append(category.name)

    subCateArr = {}

    for name in categoryArr:
        subCateArr[name] = Subcategories.objects.all().filter(category__name=name)

    context = {
        "sliders": bannerSliderQueryset,
        "whyChooseUs": whyChooseUsQueryset,
        "serviceBanner": serviceImageQueryset,
        "testimonials": testimonialQueryset,
        "specialPricing": specialPriceQueryset,
        "shopInformation": shopInforQueryset,
        "categories": categoriesQueryset,
        "subcategories": subCateArr
    }

    return render(request, 'home/index.html', context)