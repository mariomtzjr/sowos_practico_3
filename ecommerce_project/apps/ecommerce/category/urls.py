from django.urls import path
from apps.ecommerce.category.views import (
    CategoryCreate,
    CategoryList,
    CategoryUpdate,
    CategoryDelete
    )

urlpatterns = [
    path('crear/', CategoryCreate.as_view(), name="category_create"),
    path('listar/', CategoryList.as_view(), name='category_list'),
    path('editar/<int:pk>', CategoryUpdate.as_view(), name='category_edit'),
    path('eliminar/<int:pk>', CategoryDelete.as_view(), name='category_delete'),
]
