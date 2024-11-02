# Instrucciones de Instalación para wt-indicators

Este repositorio contiene el proyecto Django `wt-indicators`. Para ejecutarlo localmente, sigue los pasos detallados a continuación.

## Pasos para la Configuración

1. **Clonar el Repositorio**

   Abre una terminal y navega hasta el directorio donde deseas guardar el proyecto. Luego clona el repositorio:


   git clone https://github.com/diegotrigal/wt-indicators.git

   2. **Crear y Activar un Entorno Virtual**

En la carpeta del proyecto, crea un entorno virtual y actívalo con los siguientes comandos:

- Para sistemas **Unix** o **Mac**:

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

- Para **Windows**:

  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```

3. **Instalar Dependencias**

Asegúrate de que el entorno virtual esté activado. Instala las dependencias necesarias ejecutando:

  pip install -r requirements.txt

4. **Ejecutar el Servidor de Desarrollo**

Inicia el servidor de desarrollo local con el siguiente comando:

  python manage.py runserver

5. **Acceder a la Aplicación**

Abre un navegador y visita `http://127.0.0.1:8000/` para acceder a la aplicación.

## Disfruta

Una vez que hayas completado los pasos anteriores, deberías poder acceder y usar la aplicación `wt-indicators` localmente.

