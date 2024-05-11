# library django
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import FooterInfo, Product_women
from django.contrib.auth import authenticate, login
from .shopman import products
from django.views.decorators.http import require_POST
from django.contrib import messages

# home html
def home(request):
    footer_info = FooterInfo.objects.first()
    content = {'footer_info': footer_info}
    return render(request, 'home.html', content)

#sign up call html [API]
def signup_view(request):
    if request.method == 'POST':  
        form = SignUpForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            # In mật khẩu ra console 
            print(password)
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# sign in call html [API]
def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Username or Password incorrect👎'})
    else:
        return render(request, 'signin.html')

#shop man
def man_view(request):
    footer_info = FooterInfo.objects.first()
    context = {
        'products': products,
        'footer_info': footer_info,
    }
    return render(request, 'shopCDB/man.html', context)

#shop women
def women_view(request):
    footer_info = FooterInfo.objects.first()
    shop_women = Product_women.objects.all()
    context = {
        'shop_women': shop_women,
        'footer_info': footer_info,
    }
    return render(request, 'shopCDB/women.html', context)

#shop more
def more_view(request):
    return render(request, 'shopCDB/more.html')

#shop books
def books_view(request):
    return render(request, 'shopCDB/books.html')

#show shop man
def product_detail_view(request, product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    footer_info = FooterInfo.objects.first()
    context = {
        'footer_info': footer_info,
        'product': product,
    }
    return render(request, 'shopCDB/products.html', context)

# search show women [API]
def search_view(request):
    query = request.GET.get('q', '')
    if query:
        products = Product_women.objects.filter(name__icontains=query)
    else:
        products = Product_women.objects.all()
    return render(request, 'search.html', {'products': products})

# cart
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product_women, id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    messages.add_message(request, messages.SUCCESS, 'Product added to cart successfully👱‍♀️!')
    return redirect(request.META.get('HTTP_REFERER'))