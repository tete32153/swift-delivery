from django.shortcuts import get_object_or_404, render
from . models import Restaurant, Category

def index(request):

    restaurant_list = Restaurant.objects.all()
    category = Category.objects.all()

    context = {
        'restaurant_list': restaurant_list,
        'category': category
    }
    return render(request,'restaurant/index.html', context)


def restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu = restaurant.restaurant_menu.order_by('-name')
    return render(request, 'restaurant/restaurant.html', {'restaurant': restaurant, 'menu': menu})
