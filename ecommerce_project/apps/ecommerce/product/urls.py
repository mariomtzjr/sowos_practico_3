from django.urls import path
from apps.ecommerce.product.views import (
    ProductCreate,
    ProductList,
    ProductUpdate,
    ProductDelete
    )

urlpatterns = [
    path('crear/', ProductCreate.as_view(), name="product_create"),
    path('listar/', ProductList.as_view(), name='product_list'),
    path('editar/<int:pk>', ProductUpdate.as_view(), name='product_edit'),
    path('eliminar/<int:pk>', ProductDelete.as_view(), name='product_delete'),
]
