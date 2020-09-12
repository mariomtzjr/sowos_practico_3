from django.urls import path
from apps.ecommerce.person.views import (
    PersonCreate,
    PersonList,
    PersonUpdate,
    PersonDelete
    )

urlpatterns = [
    path('crear/', PersonCreate.as_view(), name="person_create"),
    path('listar/', PersonList.as_view(), name='person_list'),
    path('editar/<int:pk>', PersonUpdate.as_view(), name='person_edit'),
    path('eliminar/<int:pk>', PersonDelete.as_view(), name='person_delete'),
]
