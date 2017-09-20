from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Partner
from cart.forms import CartAddProductForm
from django.conf import settings

#
# def product_list(request, category_slug=None, partner_slug=None):
#     category = None
#     categories = Category.objects.all()
#     partner = Partner.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug and partner_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         partner = get_object_or_404(Partner, slug=partner_slug)
#         products = products.filter(category=category, partner=partner)
#     elif category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     elif partner_slug:
#         partner = get_object_or_404(Partner, slug=partner_slug)
#         products = products.filter(partner=partner)
#     return render(request,
#                   'shop/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'partner': partner,
#                    'products': products})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    #print("SESSION_FILE_PATH =%s " % settings.SESSION_FILE_PATH)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})