from django.contrib import admin

from .models import Restaurant
from .models import Category
from .models import Menu
from .models import Meal

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Meal)
