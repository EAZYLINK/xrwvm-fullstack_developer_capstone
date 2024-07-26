from django.contrib import admin

from .models import CarMake, CarModel
# from .models import related models


# Register your models here.
admin.site.register(CarMake)
# CarModelInline class
admin.site.register(CarModel)
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
