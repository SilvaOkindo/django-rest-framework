from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(ProductSize)

admin.site.unregister(Group)

admin.site.site_header = 'Product Review Admin'
