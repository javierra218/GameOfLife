import tkinter as tk


class ControladorJuegoDeLaVida:
    def __init__(self, raiz, modelo, vista):
        self.raiz = raiz  # Guardamos una referencia a la raíz
        self.modelo = modelo
        self.vista = vista
        self.en_ejecucion = False
        self.vista.canvas.bind("<Button-1>", self.modificar_celdas)

        # Cargar imágenes de los iconos
        self.icono_play = tk.PhotoImage(file="iconos/play.png").subsample(10)
        self.icono_pause = tk.PhotoImage(file="iconos/pause.png").subsample(10)
        self.icono_actual = self.icono_play  # Inicialmente mostramos el icono de play
        self.icono_limpiar = tk.PhotoImage(file="iconos/limpiar.png").subsample(10)

        # Crear botones con los iconos
        self.boton_actualizar = tk.Button(
            self.raiz, image=self.icono_play, command=self.toggle_simulacion
        )
        self.boton_actualizar.pack(side=tk.LEFT)
        self.boton_limpiar = tk.Button(
            self.raiz, image=self.icono_limpiar, command=self.limpiar_tablero
        )
        self.boton_limpiar.pack(side=tk.LEFT)

    def modificar_celdas(self, evento):
        x, y = evento.x // self.vista.tamano_celda, evento.y // self.vista.tamano_celda
        self.modelo.celdas[y][x] = not self.modelo.celdas[y][x]
        self.vista.dibujar_cuadricula()

    # def toggle_simulacion(self):
    #     if not self.en_ejecucion:
    #         self.en_ejecucion = True
    #         self.boton_actualizar.config(text="Pausar")
    #         self.ejecutar_simulacion()
    #     else:
    #         self.en_ejecucion = False
    #         self.boton_actualizar.config(text="Iniciar")

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
