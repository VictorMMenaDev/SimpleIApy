import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import requests
import json
import threading
import time

# URL de la API
API_URL = "https://menaylex.com/Tools/api.php"  # Cambiar por modelo api[num].php
# 0. Gemini (Default)
# 1. GPT-4o (de paga)
# 2. PaLM 2 (mantenimiento)
# 3. Claude (de paga)
# 4. LLaMA (mantenimiento)
# 5. Bard (mantenimiento)
# 6. DALL·E 3 (de paga)
# 7. Stable Diffusion (de paga)
# 8. Gato (no disp)
# 9. Flamingo (mantenimiento)
# 10. Turing-NLG (mantenimiento)
# 11. WuDao (no disp)

# Función para escribir respuesta de la IA letra por letra
def escribir_respuesta(texto):
    for letra in texto:
        chat_area.insert(tk.END, letra)
        chat_area.see(tk.END)
        ventana.update()
        time.sleep(0.02)  # Velocidad rápida (ajustable)
    chat_area.insert(tk.END, "\n\n")

# Función que ejecuta la solicitud a la API en un hilo separado
def enviar_mensaje_async(mensaje):
    barra_progreso.start()
    try:
        response = requests.post(API_URL, json={"message": mensaje}, headers={"Content-Type": "application/json"})
        data = response.json()
        barra_progreso.stop()
        barra_progreso.pack_forget()

        if 'reply' in data:
            chat_area.insert(tk.END, "IA: ")
            escribir_respuesta(data['reply'])
        else:
            chat_area.insert(tk.END, f"Error: {data.get('error', 'Respuesta desconocida')}\n\n")
    except Exception as e:
        barra_progreso.stop()
        barra_progreso.pack_forget()
        chat_area.insert(tk.END, f"Error de conexión: {str(e)}\n\n")

# Función que se llama al presionar el botón de enviar o tecla Enter
def enviar_mensaje():
    mensaje = entrada_usuario.get()
    if not mensaje:
        return

    # Mostrar mensaje del usuario en la interfaz
    chat_area.insert(tk.END, f"Tú: {mensaje}\n")
    entrada_usuario.delete(0, tk.END)
    
    # Mostrar barra de progreso mientras se espera la respuesta
    barra_progreso.pack(pady=(0, 10))
    
    # Ejecutar el envío de mensaje en un hilo separado
    threading.Thread(target=enviar_mensaje_async, args=(mensaje,), daemon=True).start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Chat con IA")
ventana.geometry("800x600")
ventana.config(bg="#F4F4F4")  # Color de fondo de la ventana

# Estilo para el chat (text area)
chat_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=90, height=20, font=("Arial", 12), bg="#FFFFFF", fg="#333333", bd=1, relief="solid")
chat_area.pack(padx=20, pady=20)
chat_area.config(state='normal')
chat_area.tag_configure("bold", font=("Arial", 12, "bold"))

# Entrada de usuario (en la parte inferior)
entrada_usuario = tk.Entry(ventana, width=75, font=("Arial", 12), bd=2, relief="solid", bg="#F9F9F9", fg="#333333")
entrada_usuario.pack(padx=20, pady=(0, 10))
entrada_usuario.bind("<Return>", lambda event: enviar_mensaje())  # Enviar con tecla Enter

# Botón de envío con estilo
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", width=15)
boton_enviar.pack(pady=(0, 10))

# Barra de progreso (oculta hasta que se haga la solicitud)
barra_progreso = ttk.Progressbar(ventana, mode='indeterminate', length=300)
barra_progreso.config(style="TProgressbar")

# Configuración de estilo de la barra de progreso
style = ttk.Style()
style.configure("TProgressbar", thickness=20, barcolor="#4CAF50")

# Iniciar la interfaz
ventana.mainloop()
