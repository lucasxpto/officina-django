from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from core.views import index, quem_somos, contato, termos, registrar

urlpatterns = [
    path('', index, name='index'),
    path('quem-somos/', quem_somos, name='quem_somos'),
    path('termos/', termos, name='termos'),
    path('contato/', contato, name='contato'),
    path('veiculos/', include('veiculo.urls')),
    path('registrar/', registrar, name='registrar'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
