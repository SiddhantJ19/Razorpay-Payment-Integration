from django.urls import path, re_path
from . import views

app_name = 'payment'
urlpatterns = [
    path('', views.payment, name='payment_api'),
    path('payment_success/', views.payment_success, name='payment_success'),
]
