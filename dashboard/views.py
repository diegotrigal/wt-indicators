# dashboard/views.py

from django.shortcuts import render
from django.http import JsonResponse
import requests


def index(request):
    try:
        # Solicitar los datos JSON de War Thunder
        state_data = requests.get("http://127.0.0.1:8111/state").json()
        indicators_data = requests.get("http://127.0.0.1:8111/indicators").json()

        # Agregar ambos conjuntos de datos al contexto
        context = {
            "state": state_data,
            "indicators": indicators_data,
        }

    except requests.RequestException as e:
        # Manejar errores en caso de que los datos no estén disponibles
        context = {"error": f"No se pudieron obtener los datos: {e}"}

    # Renderizar el template con el contexto que contiene los datos
    return render(request, "index.html", context)


# Nueva vista para retornar los datos en JSON
def get_data(request):
    try:
        state_data = requests.get("http://127.0.0.1:8111/state").json()
        indicators_data = requests.get("http://127.0.0.1:8111/indicators").json()
        data = {"state": state_data, "indicators": indicators_data}
    except requests.RequestException as e:
        data = {"error": str(e)}
    return JsonResponse(data)
