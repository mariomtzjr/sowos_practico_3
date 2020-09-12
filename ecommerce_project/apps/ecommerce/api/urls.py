from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('persons/', include('apps.ecommerce.person.urls')),
    path('customers/', include('apps.ecommerce.customer.urls')),
    path('purchases/', include('apps.ecommerce.purchase.urls')),
    path('categories/', include('apps.ecommerce.category.urls')),
    path('products/', include('apps.ecommerce.product.urls')),
    path('purchase-products/', include('apps.ecommerce.purchaseproduct.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
