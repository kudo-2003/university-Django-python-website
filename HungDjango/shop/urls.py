from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('man/', views.man_view, name='man'),
    path('women/', views.women_view, name='women'),
    path('more/', views.more_view, name='more'),
    path('books-and-notbooks/', views.books_view, name='books'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('search/', views.search_view, name='search'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
] 