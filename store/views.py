from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category


# --- USER AUTH VIEWS ---

# --- PAGE VIEWS ---

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search', '').strip()

    products = Product.objects.all()
    if selected_category:
        products = products.filter(category__name=selected_category)
    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    })

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# --- CART LOGIC ---
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        items.append({'product': product, 'quantity': quantity, 'total': item_total})
        total += item_total
    return render(request, 'store/cart.html', {'items': items, 'total': total})

# --- OPTIONAL DASHBOARD ---
def dashboard(request):
    return render(request, 'store/dashboard.html')

def update_cart_quantity(request, pk, action):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        if action == 'add':
            cart[str(pk)] += 1
        elif action == 'remove':
            cart[str(pk)] -= 1
            if cart[str(pk)] <= 0:
                del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart')

# --- CHECKOUT LOGIC ---
def checkout(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        items.append({'product': product, 'quantity': quantity, 'total': item_total})
        total += item_total

    if request.method == 'POST' and items:
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment = request.POST.get('payment_method')

        from django.utils.crypto import get_random_string
        from django.utils import timezone
        from datetime import timedelta
        order_number = f"ORD{timezone.now().strftime('%Y%m%d')}-{get_random_string(5).upper()}"
        delivery_estimate = (timezone.now() + timedelta(days=3)).strftime('%d %b, %Y')

        # Optionally, save order details to DB or send email here

        # Clear cart
        request.session['cart'] = {}
        request.session['order_number'] = order_number
        request.session['delivery_estimate'] = delivery_estimate
        return redirect('order_confirmation')

    return render(request, 'store/checkout.html', {'items': items, 'total': total})

def order_confirmation(request):
    order_number = request.session.get('order_number')
    delivery_estimate = request.session.get('delivery_estimate')

    if not order_number:
        return redirect('home') 

    request.session.pop('order_number')
    request.session.pop('delivery_estimate')

    return render(request, 'store/order_confirmation.html', {
        'order_number': order_number,
        'delivery_estimate': delivery_estimate
    })


