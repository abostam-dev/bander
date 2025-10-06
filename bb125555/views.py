from django.shortcuts import render
from commerce.models import Product


# الصفحة الرئيسية
def home_view(request):
    # جلب جميع المنتجات من قاعدة البيانات
    products = Product.objects.all()
    # تمرير المنتجات لقالب home.html
    return render(request, "home.html", {"products": products})
