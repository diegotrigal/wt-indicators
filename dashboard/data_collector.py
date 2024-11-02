import requests
import time
from threading import Thread

data_store = {"state": {}, "indicators": {}}
refresh_time = 500  # Tiempo de refresco en milisegundos


def get_all_flight_data():
    global data_store
    try:
        state_data = requests.get("http://127.0.0.1:8111/state").json()
        indicator_data = requests.get("http://127.0.0.1:8111/indicators").json()
        data_store["state"] = state_data
        data_store["indicators"] = indicator_data
    except requests.RequestException as e:
        print("Error al obtener los datos:", e)
        data_store = {"error": str(e)}


def start_data_collection():
    while True:
        get_all_flight_data()
        time.sleep(refresh_time / 1000)


def start_data_collector_thread():
    collector_thread = Thread(target=start_data_collection, daemon=True)
    collector_thread.start()
