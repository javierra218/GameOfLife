import tkinter as tk
from modelo import ModeloJuegoDeLaVida
from vista import VistaJuegoDeLaVida
from controlador import ControladorJuegoDeLaVida

raiz = tk.Tk()
raiz.title("Juego de la Vida")
modelo = ModeloJuegoDeLaVida()
vista = VistaJuegoDeLaVida(raiz, modelo)
controlador = ControladorJuegoDeLaVida(raiz, modelo, vista)
vista.dibujar_cuadricula()
# Bloquear el cambio de tamaño de la ventana
raiz.resizable(width=False, height=False)
raiz.mainloop()
