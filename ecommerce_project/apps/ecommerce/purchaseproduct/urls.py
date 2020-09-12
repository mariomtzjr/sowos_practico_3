from django.urls import path
from apps.ecommerce.purchaseproduct.views import (
    PurchaseProductsCreate,
    PurchaseProductsList,
    PurchaseProductsUpdate,
    PurchaseProductsDelete
    )

urlpatterns = [
    path('crear/', PurchaseProductsCreate.as_view(), name="purchaseproduct_create"),
    path('listar/', PurchaseProductsList.as_view(), name='purchaseproduct_list'),
    path('editar/<int:pk>', PurchaseProductsUpdate.as_view(), name='purchaseproduct_edit'),
    path('eliminar/<int:pk>', PurchaseProductsDelete.as_view(), name='purchaseproduct_delete'),
]
