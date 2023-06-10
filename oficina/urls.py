from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, quem_somos, contato

urlpatterns = [
    path('', index, name='index'),
    path('quem-somos/', quem_somos, name='quem_somos'),
    path('contato/', contato, name='contato'),
    path('veiculos/', include('veiculo.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
