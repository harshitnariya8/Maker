from django.contrib import admin
from .models import RestaurantAccount,Product,Category,Table

# Register your models here.
admin.site.register(RestaurantAccount)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Table)