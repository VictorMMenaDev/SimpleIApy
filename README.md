# Chat con IA - Mini Script de Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Visita Menaylex.com para más herramientas y recursos.**

Este repositorio contiene un mini script en Python con una interfaz gráfica simple (Tkinter) para interactuar con la API de chat de Mena. Permite enviar mensajes de texto y recibir respuestas generadas por un modelo de IA (configurado en el backend de la API).

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
    - [Configuración](#configuración)
    - [Ejecución](#ejecución)
    - [Interactuando con la IA](#interactuando-con-la-ia)
- [Manejo de Errores](#manejo-de-errores)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Soporte](#soporte)
- [Autor](#autor)

## Características

* **Interfaz Gráfica Simple:** Utiliza Tkinter para una interacción intuitiva mediante una ventana de chat.
* **Envío de Mensajes:** Permite al usuario ingresar y enviar mensajes de texto a la API.
* **Recepción de Respuestas de la IA:** Muestra las respuestas generadas por la IA en la ventana de chat con un efecto de escritura gradual.
* **Indicador de Carga:** Incorpora una barra de progreso para indicar que se está esperando la respuesta de la API.
* **Hilos para Operaciones Asíncronas:** Utiliza hilos para evitar bloquear la interfaz de usuario mientras se espera la respuesta de la API.
* **Fácil de Usar:** Diseño simple y directo para una interacción rápida con la IA.

## Requisitos

* **Python 3.x:** El script está desarrollado y probado con Python 3.
* **Biblioteca `tkinter`:** Utilizada para la interfaz gráfica. Generalmente viene instalada con Python.
* **Biblioteca `requests`:** Necesaria para realizar solicitudes HTTP a la API. Puedes instalarla con:
    ```bash
    pip install requests
    ```
* **Acceso a la API:** Necesitarás acceso a la API en la URL `https://menaylex.com/Tools/api.php`.

## Instalación

1.  **Clona este repositorio (opcional):** Si deseas tener una copia local del script y posiblemente contribuir, puedes clonar el repositorio:
    ```bash
    git clone [https://github.com/sindresorhus/del](https://github.com/sindresorhus/del)
    cd [nombre del repositorio]
    ```
2.  **Descarga el script:** Alternativamente, puedes simplemente descargar el archivo Python (por ejemplo, `chat_ia.py`) directamente.

## Uso

### Configuración

Antes de ejecutar el script, asegúrate de tener la biblioteca `requests` instalada. La URL de la API (`API_URL`) ya está configurada dentro del script:

```python
API_URL = "[https://menaylex.com/Tools/api.php](https://menaylex.com/Tools/api.php)"
