from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('arquivos/', views.arquivos, name='arquivos'),
    path('arquivos/remover/<int:id>', views.remover, name='remover'),
    path('arquivos/alterar/<int:id>', views.alterar, name='alterar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)