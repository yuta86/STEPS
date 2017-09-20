from django.contrib import admin
from .models import Category, Product, Partner


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
# prepopulated_fields, чтобы указать поля, в которых значение автоматически задается с использованием значения других полей

admin.site.register(Category, CategoryAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}
# prepopulated_fields, чтобы указать поля, в которых значение автоматически задается с использованием значения других полей

admin.site.register(Partner, PartnerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'partner', 'category', 'image', 'description', 'price', 'stock', 'available',
                    'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
# prepopulated_fields, чтобы указать поля, в которых значение автоматически задается с использованием значения других полей

admin.site.register(Product, ProductAdmin)
