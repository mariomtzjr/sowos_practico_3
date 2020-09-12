from django.urls import path
from apps.ecommerce.customer.views import (
    CustomerCreate,
    CustomerList,
    CustomerUpdate,
    CustomerDelete
    )

urlpatterns = [
    path('crear/', CustomerCreate.as_view(), name="customer_create"),
    path('listar/', CustomerList.as_view(), name='customer_list'),
    path('editar/<int:pk>', CustomerUpdate.as_view(), name='customer_edit'),
    path('eliminar/<int:pk>', CustomerDelete.as_view(), name='customer_delete'),
]
