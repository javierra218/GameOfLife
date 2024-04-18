import tkinter as tk

class ModeloJuegoDeLaVida:
    def __init__(self, filas=50, columnas=50):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [[False] * columnas for _ in range(filas)]
    
    def actualizar_celdas(self):
        nuevas_celdas = [[False] * self.columnas for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                vecinos_vivos = self.contar_vecinos_vivos(i, j)
                nuevas_celdas[i][j] = (vecinos_vivos == 3) or (self.celdas[i][j] and vecinos_vivos == 2)
        self.celdas = nuevas_celdas

    def contar_vecinos_vivos(self, fila, columna):
        conteo = 0
        for i in range(max(0, fila - 1), min(self.filas, fila + 2)):
            for j in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                if (i != fila or j != columna) and self.celdas[i][j]:
                    conteo += 1
        return conteo

    def limpiar_celdas(self):
        self.celdas = [[False] * self.columnas for _ in range(self.filas)]

class VistaJuegoDeLaVida:
    def __init__(self, maestro, modelo, tamano_celda=10):
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

class ControladorJuegoDeLaVida:
    def __init__(self, raiz, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.en_ejecucion = False
        self.vista.canvas.bind("<Button-1>", self.modificar_celdas)
        self.boton_actualizar = tk.Button(raiz, text="Iniciar", command=self.toggle_simulacion)
        self.boton_actualizar.pack(side=tk.LEFT)
        self.boton_limpiar = tk.Button(raiz, text="Limpiar", command=self.limpiar_tablero)
        self.boton_limpiar.pack(side=tk.LEFT)
    
    def modificar_celdas(self, evento):
        x, y = evento.x // self.vista.tamano_celda, evento.y // self.vista.tamano_celda
        self.modelo.celdas[y][x] = not self.modelo.celdas[y][x]
        self.vista.dibujar_cuadricula()

    def toggle_simulacion(self):
        if not self.en_ejecucion:
            self.en_ejecucion = True
            self.boton_actualizar.config(text="Pausar")
            self.ejecutar_simulacion()
        else:
            self.en_ejecucion = False
            self.boton_actualizar.config(text="Iniciar")
    
    def ejecutar_simulacion(self):
        if self.en_ejecucion:
            self.modelo.actualizar_celdas()
            self.vista.dibujar_cuadricula()
            raiz.after(100, self.ejecutar_simulacion)

    def limpiar_tablero(self):
        self.modelo.limpiar_celdas()
        self.vista.dibujar_cuadricula()

raiz = tk.Tk()
raiz.title("Juego de la Vida")
modelo = ModeloJuegoDeLaVida()
vista = VistaJuegoDeLaVida(raiz, modelo)
controlador = ControladorJuegoDeLaVida(raiz, modelo, vista)
vista.dibujar_cuadricula()
raiz.mainloop()
