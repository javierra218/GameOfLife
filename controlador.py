import tkinter as tk
from tkinter import filedialog
import json


class ControladorJuegoDeLaVida:
    def __init__(self, raiz, modelo, vista):
        self.raiz = raiz  # Guardamos una referencia a la raíz
        self.modelo = modelo
        self.vista = vista
        self.en_ejecucion = False
        self.vista.canvas.bind("<Button-1>", self.modificar_celdas)

        # Cargar imágenes de los iconos
        self.icono_play = tk.PhotoImage(file="iconos/play.png").subsample(15)
        self.icono_pause = tk.PhotoImage(file="iconos/pause.png").subsample(15)
        self.icono_actual = self.icono_play  # Inicialmente mostramos el icono de play
        self.icono_limpiar = tk.PhotoImage(file="iconos/limpiar.png").subsample(15)
        self.icono_guardar = tk.PhotoImage(file="iconos/guardar.png").subsample(15)
        self.icono_cargar = tk.PhotoImage(file="iconos/cargar.png").subsample(15)
        
        # Crear un frame para los botones con iconos
        self.frame_botones = tk.Frame(self.raiz)
        self.frame_botones.pack()

        # Crear botones con los iconos dentro del frame
        self.boton_actualizar = tk.Button(
            self.frame_botones, image=self.icono_play, command=self.toggle_simulacion
        )
        self.boton_actualizar.pack(side=tk.LEFT)
        self.boton_limpiar = tk.Button(
            self.frame_botones, image=self.icono_limpiar, command=self.limpiar_tablero
        )
        self.boton_limpiar.pack(side=tk.LEFT)
        
        # Botones de guardar y cargar
        self.boton_guardar = tk.Button(
            self.frame_botones, image=self.icono_guardar, command=self.guardar_patron
        )
        self.boton_guardar.pack(side=tk.LEFT)
        self.boton_cargar = tk.Button(
            self.frame_botones, image=self.icono_cargar, command=self.cargar_patron
        )
        self.boton_cargar.pack(side=tk.LEFT)

    def modificar_celdas(self, evento):
        x, y = evento.x // self.vista.tamano_celda, evento.y // self.vista.tamano_celda
        self.modelo.celdas[y][x] = not self.modelo.celdas[y][x]
        self.vista.dibujar_cuadricula()


    def toggle_simulacion(self):
        self.en_ejecucion = not self.en_ejecucion  # Alternamos entre pausa y ejecución
        if self.en_ejecucion:
            self.boton_actualizar.config(
                image=self.icono_pause
            )  # Mostramos el icono de pause
            self.ejecutar_simulacion()
        else:
            self.boton_actualizar.config(
                image=self.icono_play
            )  # Mostramos el icono de play

    def ejecutar_simulacion(self):
        if self.en_ejecucion:
            self.modelo.actualizar_celdas()
            self.vista.dibujar_cuadricula()
            self.raiz.after(100, self.ejecutar_simulacion)

    def limpiar_tablero(self):
        self.modelo.limpiar_celdas()
        self.vista.dibujar_cuadricula()
        
    
    
    def guardar_patron(self):
        try:
            nombre_archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivo JSON", "*.json")])
            if nombre_archivo:
                with open(nombre_archivo, 'w') as archivo:
                    json.dump(self.modelo.celdas, archivo, indent=4)
                    print(f"Patrón guardado en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el patrón: {e}")

    def cargar_patron(self):
        try:
            nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
            if nombre_archivo:
                with open(nombre_archivo, 'r') as archivo:
                    self.modelo.celdas = json.load(archivo)
                    self.vista.dibujar_cuadricula()
                    print(f"Patrón cargado desde {nombre_archivo}")
        except FileNotFoundError:
            print("El archivo especificado no existe.")
        except Exception as e:
            print(f"Error al cargar el patrón: {e}")
