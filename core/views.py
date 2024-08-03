from django.http import JsonResponse


def index(request):
    return JsonResponse({'api_version': '1.0', "api_name": "API Escola"}) 