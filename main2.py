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
raiz.mainloop()
