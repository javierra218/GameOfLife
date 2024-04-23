import tkinter as tk


class VistaJuegoDeLaVida:
    def __init__(self, maestro, modelo, tamano_celda=14):
        self.modelo = modelo
        self.tamano_celda = tamano_celda
        self.canvas = tk.Canvas(maestro, width=modelo.columnas * tamano_celda, height=modelo.filas * tamano_celda, bg='white')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def dibujar_cuadricula(self):
        self.canvas.delete("all")
        for i in range(self.modelo.filas):
            for j in range(self.modelo.columnas):
                color = "green" if self.modelo.celdas[i][j] else "white"
                self.canvas.create_rectangle(j * self.tamano_celda, i * self.tamano_celda,
                                             j * self.tamano_celda + self.tamano_celda, i * self.tamano_celda + self.tamano_celda,
                                             fill=color, outline="gray")
