from django.urls import path
from shop_project.views import shops
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', shops.product_list, name='product_list'),
    path('<slug:category_slug>/', shops.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', shops.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', shops.register, name='register'),
]
