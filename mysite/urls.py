from django.urls import path, include
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('products/', views.product_details, name='product-details'),
]
