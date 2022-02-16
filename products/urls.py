
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new_product),
    path('detail/<int:id>', views.product_detail)
]
