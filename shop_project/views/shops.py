from django.shortcuts import render, get_object_or_404
from shop_project.models import Category, Product, Review
from shop_project.forms import ReviewForm
from django.shortcuts import redirect

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
            return redirect('products:product_detail', id=id, slug=slug)
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, "detail.html", context)
