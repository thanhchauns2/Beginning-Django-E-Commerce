from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

admin.autodiscover() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('', include("catalog.urls")),
    path('', include("cart.urls")),
    path('', include("accounts.urls")),
    path('', include("django.contrib.auth.urls")), # <-- added
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ecomstore.views.file_not_found_404' 
handler500 = 'ecomstore.views.file_not_found_500' 