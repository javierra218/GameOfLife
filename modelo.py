class ModeloJuegoDeLaVida:
    def __init__(self, filas=40, columnas=40):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [[False] * columnas for _ in range(filas)]
        # self.celdas = []
        # for _ in range(filas):
        #     fila = []
        #     for _ in range(columnas):
        #         fila.append(False)
        #         self.celdas.append(fila)

    
    def actualizar_celdas(self):
        nuevas_celdas = [[False] * self.columnas for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                vecinos_vivos = self.contar_vecinos_vivos(i, j)
                nuevas_celdas[i][j] = (vecinos_vivos == 3) or (self.celdas[i][j] and vecinos_vivos == 2)
        self.celdas = nuevas_celdas

    def contar_vecinos_vivos(self, fila, columna):
        conteo = 0
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if (i != fila or j != columna) and self.celdas[i % self.filas][j % self.columnas]:
                    conteo += 1
        return conteo

    def limpiar_celdas(self):
        self.celdas = [[False] * self.columnas for _ in range(self.filas)]
        # self.celdas = []
        # for _ in range(self.filas):
        #     fila = []
        #     for _ in range(self.columnas):
        #         fila.append(False)
        #     self.celdas.append(fila)