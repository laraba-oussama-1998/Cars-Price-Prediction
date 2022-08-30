from django.urls import path
from .views import CarPriceList,CarPriceDetail
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

urlpatterns = [
    path('', CarPriceList.as_view(), name="carprice"),
    path('<int:pk>/', CarPriceDetail.as_view(), name="carprice_detail"),



]