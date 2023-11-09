from django.urls import path
from shop_project.views import shops

urlpatterns = [
    path('', shops.product_list, name='product_list'),
    path('<slug:category_slug>/', shops.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', shops.product_detail, name='product_detail'),
]
