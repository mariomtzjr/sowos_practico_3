from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.ecommerce.views import PersonCreate


urlpatterns = [
    path('personas/crear', PersonCreate.as_view(), name="person_create"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
