# urls.py
from django.urls import path
from .views import index, salvar_dados_view

urlpatterns = [
    path('', index, name='index'),                    # GET /
    path('enviar_dados/', salvar_dados_view),         # POST (via fetch)
]
