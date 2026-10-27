import tkinter as tk
from tkinter import messagebox
import random
import string
import subprocess
import os
import sys
from PIL import Image

def preparar_icono_y_ruta(nombre_imagen_jpg, nombre_icono_ico):
    """ Convierte tu imagen JPG a .ico automáticamente y de forma gratuita al arrancar """
    try:
        base_path = os.path.abspath(".")
        path_jpg = os.path.join(base_path, nombre_imagen_jpg)
        path_ico = os.path.join(base_path, nombre_icono_ico)
        
        # Si la imagen JPG existe y el .ico todavía no, lo creamos al instante gratis
        if os.path.exists(path_jpg) and not os.path.exists(path_ico):
            img = Image.open(path_jpg)
            img.save(path_ico, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
            
        if os.path.exists(path_ico):
            return path_ico
    except Exception:
        pass
    return None

def generar_lote():
    try:
        cantidad = int(entrada_cantidad.get())
        if cantidad <= 0:
            raise ValueError
            
        longitud = int(entrada_longitud.get())
        if longitud < 4:
            messagebox.showerror("Error", "La longitud mínima recomendada es de 4 caracteres.")
            return
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos en cantidad y longitud.")
        return

    letras_y_numeros = string.ascii_letters + string.digits
    simbolos_seguros = "!@#$%^&*-_."
    
    if var_simbolos.get() == 1:
        caracteres = letras_y_numeros + simbolos_seguros
    else:
        caracteres = letras_y_numeros
    
    cuadro_texto.delete("1.0", tk.END)
    
    passwords = []
    for i in range(cantidad):
        pwd = "".join(random.choice(caracteres) for _ in range(longitud))
        passwords.append(f"Contraseña {i+1}: {pwd}")
    
    cuadro_texto.insert(tk.END, "\n".join(passwords))
    etiqueta_estado.config(text=f"¡Se generaron {cantidad} claves de {longitud} caracteres!", fg="#2ecc71")

def copiar_todo():
    texto_completo = cuadro_texto.get("1.0", tk.END).strip()
    if texto_completo:
        try:
            process = subprocess.Popen(['clip.exe'], stdin=subprocess.PIPE, text=True, encoding='utf-8')
            process.communicate(input=texto_completo)
            etiqueta_estado.config(text="¡Todas las contraseñas copiadas a Windows con éxito!", fg="#2ecc71")
        except Exception as e:
            etiqueta_estado.config(text="Error al copiar al portapapeles", fg="#e74c3c")
    else:
        etiqueta_estado.config(text="No hay contraseñas para copiar", fg="#e74c3c")

# Ventana principal
ventana = tk.Tk()
ventana.title("Generador Masivo Inteligente - HP OMEN")
ventana.geometry("500x640")
ventana.config(bg="#1e1e1e")

# CONVERSIÓN AUTOMÁTICA DEL JPG AL ICONO
# (Asegúrate de que tu imagen se llame exactamente igual que el primer texto, o cámbialo aquí si tiene otro nombre)
icono_generado = preparar_icono_y_ruta("imagen_candado.jpg", "icono_automatico.ico")
if icono_generado:
    try:
        ventana.iconbitmap(icono_generado)
    except Exception:
        pass

# Título
titulo = tk.Label(ventana, text="Generador Masivo de Contraseñas", font=("Arial", 13, "bold"), fg="white", bg="#1e1e1e")
titulo.pack(pady=10)

# Marco para la cantidad
frame_cantidad = tk.Frame(ventana, bg="#1e1e1e")
frame_cantidad.pack(pady=5)

label_cant = tk.Label(frame_cantidad, text="¿Cuántas contraseñas quieres generar?:", font=("Arial", 10), fg="white", bg="#1e1e1e")
label_cant.pack(side=tk.LEFT, padx=5)

entrada_cantidad = tk.Entry(frame_cantidad, font=("Arial", 11), justify="center", width=8)
entrada_cantidad.insert(0, "10")
entrada_cantidad.pack(side=tk.LEFT, padx=5)

# Marco para la longitud de los caracteres
frame_longitud = tk.Frame(ventana, bg="#1e1e1e")
frame_longitud.pack(pady=5)

label_long = tk.Label(frame_longitud, text="¿De cuántos caracteres cada contraseña?:", font=("Arial", 10), fg="white", bg="#1e1e1e")
label_long.pack(side=tk.LEFT, padx=5)

entrada_longitud = tk.Entry(frame_longitud, font=("Arial", 11), justify="center", width=8)
entrada_longitud.insert(0, "14")
entrada_longitud.pack(side=tk.LEFT, padx=5)

# Casilla de verificación para los símbolos
var_simbolos = tk.IntVar(value=1)
check_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos seguros (!@#$...) - Desmarcar para solo letras y números", 
                                variable=var_simbolos, font=("Arial", 9), fg="white", bg="#1e1e1e", selectcolor="#333333", activebackground="#1e1e1e", activeforeground="white")
check_simbolos.pack(pady=8)

# Botón para generar el lote
boton_generar = tk.Button(ventana, text="> GENERAR LOTE MASIVO <", font=("Arial", 11, "bold"), bg="#007acc", fg="white", bd=0, padx=10, pady=6, command=generar_lote)
boton_generar.pack(pady=5)

# Cuadro grande de texto con barra lateral
cuadro_texto = tk.Text(ventana, font=("Courier", 10), width=55, height=14)
cuadro_texto.pack(pady=5)

# Botón para copiar todo
boton_copiar = tk.Button(ventana, text="> COPIAR TODAS A WINDOWS <", font=("Arial", 10, "bold"), bg="#28a745", fg="white", bd=0, padx=10, pady=6, command=copiar_todo)
boton_copiar.pack(pady=10)

# Etiqueta de estado
etiqueta_estado = tk.Label(ventana, text="", font=("Arial", 9), bg="#1e1e1e", fg="white")
etiqueta_estado.pack(pady=5)

ventana.mainloop()