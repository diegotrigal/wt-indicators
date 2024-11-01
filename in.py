import requests
import time

# Configuración del tiempo de actualización en milisegundos
refresh_time = 500  # Tiempo de refresco en milisegundos


# Función para obtener los valores de Vy, pitch y IAS
def get_flight_data():
    try:
        # Obtener datos del JSON en http://127.0.0.1:8111/state
        state_data = requests.get("http://127.0.0.1:8111/state").json()
        vy = state_data.get("Vy, m/s", "N/A")  # Velocidad vertical en m/s
        pitch = state_data.get("pitch 1, deg", None)  # Ángulo de cabeceo en grados

        # Obtener datos del segundo JSON en http://127.0.0.1:8111/indicators
        indicator_data = requests.get("http://127.0.0.1:8111/indicators").json()
        if pitch is None:
            pitch = indicator_data.get(
                "aviahorizon_pitch", "N/A"
            )  # Usar aviahorizon_pitch si pitch 1 no está disponible
        ias = state_data.get("IAS, km/h", "N/A")  # Velocidad indicada en km/h

        return vy, pitch, ias

    except requests.RequestException as e:
        print("Error al obtener los datos:", e)
        return "N/A", "N/A", "N/A"


# Bucle principal para mostrar los datos en tiempo real
while True:
    vy, pitch, ias = get_flight_data()
    # Mostrar los valores en un solo renglón, sobrescribiendo la línea anterior
    print(f"Vy (m/s): {vy} | Pitch (deg): {pitch} | IAS (km/h): {ias}", end="\r")

    # Espera el tiempo configurado antes de actualizar
    time.sleep(refresh_time / 1000)
