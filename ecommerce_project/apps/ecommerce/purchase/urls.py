from django.urls import path
from apps.ecommerce.purchase.views import (
    PurchaseCreate,
    PurchaseList,
    # PurchaseUpdate,
    PurchaseDelete
    )

urlpatterns = [
    path('crear/', PurchaseCreate.as_view(), name="purchase_create"),
    path('listar/', PurchaseList.as_view(), name='purchase_list'),
    # path('editar/<int:pk>', PurchaseUpdate.as_view(), name='purchase_edit'),
    path('eliminar/<int:pk>', PurchaseDelete.as_view(), name='purchase_delete'),
]
