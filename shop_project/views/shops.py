from django.shortcuts import render, get_object_or_404
from shop_project.models import Category, Product, Review
from shop_project.forms import ReviewForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category_slug': category_slug,
        'categories': categories,
        'products': products
    }
    return render(request, "list.html", context)


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', id=product.id, slug=product.slug)
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, "detail.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop_project:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})