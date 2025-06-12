# Proyecto de Sistemas Operativos – Sesión 2: El Sindicato de Contenedores

## Escenario
> A partir del ejercicio de la sesión anterior, ahora deberán construir la aplicación completa, agregando un backend y conectándolo a la base de datos

## Objetivos
- Crear un `docker-compose.yml` que incluya:
  - Frontend (`app.py`) - a partir de un Dockerfile
  - Backend (`backend.py`) - a partir de un Dockerfile
  - MariaDB (pueden buscar la imagen desde Dockerhub)
- El backend debe:
  - Conectarse a MariaDB usando variables de entorno (`DB_HOST`, `DB_USER`, etc.)
  - Exponerse en el puerto 5001
- El frontend debe obtener datos desde el backend

## Archivos proporcionados
- `frontend.py`
- `requirements.txt` del frontend
- `backend.py`
- `requirements.txt` del backend

## Tips
- Definan redes y variables de entorno en el archivo de Docker Compose
- Utilicen los nombres de servicios como hostnames (`backend`, `mariadb`, etc.)
- Comprueben conectividad entre servicios con `curl` y `docker-compose logs`, además de visualizar el frontend desde el navegador

## Entregables
- `docker-compose.yml`
- Evidencia de funcionamiento entre servicios (pantallazos, logs o curl)

## Documentación

https://docs.docker.com/get-started/workshop/07_multi_container/
