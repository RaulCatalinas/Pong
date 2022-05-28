import os
import sys
from tkinter import Button, Label, Tk
from tkinter import messagebox

import pygame as pg
from pygame import QUIT

# Colores en hexadecimal
azulOscuro = "#000033"
azul = "#00FFFF"
rojoOscuro = "#330000"
rojo = "#FF0000"
negro = "#000000"
azulEtiquetas = "#33FFFF"
verdeEtiquetas = "#00CC66"
blanco = "#FFFFFF"
amarillo = "#FFFF00"
amarilloOscuro = "#333300"
verdeOscuro = "#003300"
verde = "#00FF00"
naranjaOscuro = "#331900"
naranja = "#FF8000"


# Clase que controla el cierre del juego
class Salir:
    """La clase Salir controla el cierre del juego, muestra un diálogo de confirmación de que si el usuario está
    seguro de cerrar el juego, y si da a que si está seguro entonces destruye la ventana actual"""

    def FuncionSalir(self, ventanaACerrar):
        self.Tk = ventanaACerrar

        self.cerrar = messagebox.askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            self.Tk.destroy()

    def FuncionSalirPygame(self, ventanaACerrar):
        self.Tk = ventanaACerrar

        self.cerrar = messagebox.askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            jugando = False
            pg.quit()
            sys.exit()


# Clase que cambia el color de los botones al pasar el ratón por encima
class CambiarColor:
    """
    Clase que cambia el color de los botones al pasar el ratón por encima.
    """

    def FuncionCambiarColor(self, button, colorRatonDentro, colorRatonFuera):
        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=colorRatonDentro, cursor="hand2"),
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


# Clase que crea los botones, los coloca en pantalla y los cambia de color al pasar el ratón por encima de ellos
class Botones:
    """
    Clase que crea los botones, los coloca en la ventana y los cambia de color al pasar el ratón por encima de ellos.
    """

    class BotonPosicionAbsoluta:
        def __init__(
                self,
                texto,
                y,
                ancho,
                colorFondo,
                funcion,
                fuente,
                tamañoFuente,
                ventana,
                colorRatonDentro,
                colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función "CambiarColor" para cambiar el color del botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            self.cambiarColor = CambiarColor()

            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            self.boton = Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.boton.pack(pady=self.y)

            self.cambiarColor.FuncionCambiarColor(
                self.boton,
                self.colorRatonDentro,
                self.colorRatonFuera
            )

    class BotonPosicionRelativa:
        def __init__(
                self,
                texto,
                x,
                y,
                ancho,
                colorFondo,
                funcion,
                fuente,
                tamañoFuente,
                ventana,
                colorRatonDentro,
                colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función "CambiarColor" para cambiar el color del botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param x - La distancia entre el botón y el widget anterior.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            self.cambiarColor = CambiarColor()

            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            self.boton = Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.boton.place(x=x, y=y)

            self.cambiarColor.FuncionCambiarColor(
                self.boton,
                self.colorRatonDentro,
                self.colorRatonFuera
            )


# Clase que crea los labels y los coloca en pantalla
class Etiqueta:
    def __init__(
            self,
            texto,
            y,
            ancho,
            colorFondo,
            fuente,
            tamañoFuente,
            ventana
    ):
        """
        Crea una etiqueta con los parámetros dados y luego la coloca en la ventana.
        @param texto - El texto que se mostrará en la etiqueta.
        @param y - La posición del eje y de la etiqueta.
        @param ancho - El ancho de la etiqueta.
        @param colorFondo - El color de fondo de la etiqueta.
        @param fuente - La fuente a utilizar.
        @param tamañoFuente - Tamaño de la fuente.
        """
        # Crea una etiqueta con los parámetros dados
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana

        # Crear la etiqueta
        self.etiqueta = Label(
            self.ventana,
            text=self.texto,
            font=(self.fuente, self.tamañoFuente),
            width=self.ancho,
            bg=self.colorFondo,
        )
        # Colocar la etiqueta en la ventana
        self.etiqueta.pack(pady=self.y)


# Clase principal del programa.
class Main:
    """
    Clase principal del programa.
    """

    def FuncionMain(self):
        # Instancias de las clases
        self.salir = Salir()
        self.cambiarColor = CambiarColor()
        self.controles = Controles()
        self.boton = Botones()
        self.jugar = Jugar()
        self.creditos = Creditos()

        # Creación de la ventana
        self.ventana = Tk()
        self.ventana.title("Pong")
        self.ventana.resizable(False, False)
        self.ventana.config(bg=negro)
        self.ventana.iconbitmap("./Images/icono.ico")

        # Centrar ventana
        self.ancho_ventana = 1280
        self.alto_ventana = 720
        self.x_ventana = self.ventana.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
                str(self.ancho_ventana)
                + "x"
                + str(self.alto_ventana)
                + "+"
                + str(self.x_ventana)
                + "+"
                + str(self.y_ventana)
        )
        self.ventana.geometry(self.posicion)

        # Crear la etiqueta del título
        self.etiquetaTitulo = Etiqueta(
            "Pong",
            10,
            46,
            azulEtiquetas,
            "Helvetica",
            50,
            self.ventana,
        )

        # Crear botones
        self.botonJugar = self.boton.BotonPosicionAbsoluta(
            "Jugar",
            25,
            30,
            verdeOscuro,
            lambda: [
                self.ventana.destroy(),
                self.jugar.FuncionJugar(),
            ],
            "Helvetica",
            30,
            self.ventana,
            verde,
            verdeOscuro,
        )

        self.botonControles = self.boton.BotonPosicionAbsoluta(
            "Controles",
            30,
            30,
            azulOscuro,
            lambda: [
                self.ventana.destroy(),
                self.controles.FuncionControles(),
            ],
            "Helvética",
            30,
            self.ventana,
            azul,
            azulOscuro,
        )

        self.botonCreditos = self.boton.BotonPosicionAbsoluta(
            "Créditos",
            35,
            30,
            amarilloOscuro,
            lambda: [
                self.ventana.destroy(),
                self.creditos.FuncionCreditos(),
            ],
            "Helvetica",
            30,
            self.ventana,
            amarillo,
            amarilloOscuro,
        )

        self.botonSalir = self.boton.BotonPosicionAbsoluta(
            "Salir",
            30,
            30,
            rojoOscuro,
            lambda: self.salir.FuncionSalir(self.ventana),
            "Helvética",
            30,
            self.ventana,
            rojo,
            rojoOscuro,
        )

        # Actualizar ventana
        self.ventana.mainloop()


# Clase que controla que se muestren los controles en pantalla.
class Controles:
    """
    Clase que controla que se muestren los controles en pantalla.
    """

    def FuncionControles(self):
        # Instancias de las clases
        self.salir = Salir()
        self.main = Main()
        self.boton = Botones()
        self.creditos = Creditos()

        # Creación de la ventana
        self.ventanaControles = Tk()
        self.ventanaControles.title("Pong")
        self.ventanaControles.resizable(False, False)
        self.ventanaControles.config(bg=negro)
        self.ventanaControles.iconbitmap("./Images/icono.ico")

        # Centrar ventana
        self.ancho_ventana = 1280
        self.alto_ventana = 720
        self.x_ventana = self.ventanaControles.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.ventanaControles.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
                str(self.ancho_ventana)
                + "x"
                + str(self.alto_ventana)
                + "+"
                + str(self.x_ventana)
                + "+"
                + str(self.y_ventana)
        )
        self.ventanaControles.geometry(self.posicion)

        # Etiquetas
        self.etiquetaControles = Etiqueta(
            "Controles",
            10,
            46,
            azulEtiquetas,
            "Helvetica",
            50,
            self.ventanaControles,
        )

        self.etiquetaJ1 = Etiqueta(
            "Controles de jugador 1",
            20,
            20,
            blanco,
            "Helvetica",
            30,
            self.ventanaControles,
        )

        self.etiquetaControlesJ1 = Etiqueta(
            "W - Moverse hacia arriba\nS - Moverse hacia abajo",
            20,
            20,
            verdeEtiquetas,
            "Helvetica",
            28,
            self.ventanaControles,
        )

        self.etiquetaJ2 = Etiqueta(
            "Controles de jugador 2",
            20,
            20,
            blanco,
            "Helvetica",
            20,
            self.ventanaControles,
        )

        self.etiquetaControlesJ2 = Etiqueta(
            "Flecha arriba - Moverse hacia arriba\nFlecha abajo - Moverse hacia abajo",
            20,
            30,
            verdeEtiquetas,
            "Helvetica",
            28,
            self.ventanaControles,
        )

        self.botonVolverAlMenu = self.boton.BotonPosicionRelativa(
            "Volver al menú",
            20,
            100,
            13,
            amarilloOscuro,
            lambda: [
                self.ventanaControles.destroy(),
                self.main.FuncionMain(),
            ],
            "Helvetica",
            30,
            self.ventanaControles,
            amarillo,
            amarilloOscuro,
        )

        self.botonCreditos = self.boton.BotonPosicionRelativa(
            "Créditos",
            20,
            218,
            13,
            naranjaOscuro,
            lambda: [
                self.ventanaControles.destroy(),
                self.creditos.FuncionCreditos(),
            ],
            "Helvetica",
            30,
            self.ventanaControles,
            naranja,
            naranjaOscuro,
        )

        self.botonSalir = self.boton.BotonPosicionRelativa(
            "Salir",
            20,
            330,
            13,
            rojoOscuro,
            lambda: [
                self.salir.FuncionSalir(self.ventanaControles),
            ],
            "Helvetica",
            30,
            self.ventanaControles,
            rojo,
            rojoOscuro,
        )

        # Actualizar ventana
        self.ventanaControles.mainloop()


# Clase que controla el juego.
class Jugar:
    """
    Clase que controla el juego.
    """

    def __init__(self):
        """
        Inicialización de pygame.
        Carga de los sprites.
        Generación de la variable que controla el bucle principal del juego.
        """
        pg.init()
        self.icono = pg.image.load("./Images/icono.ico")
        self.jugar = True

    def FuncionJugar(self):
        # Instancias de las clases
        self.salir = Salir()
        self.main = Main()
        self.boton = Botones()

        # Creación de la ventana
        self.ventanaJuego = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Pong")
        self.ventanaJuego.fill(negro)
        pg.display.set_icon(self.icono)

        # Centrar ventana
        os.environ['SDL_VIDEO_CENTRED'] = '1'

        # Bucle principal del juego
        while self.jugar:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.salir.FuncionSalirPygame(self.ventanaJuego)

            # Limitar FPS
            pg.time.Clock().tick(60)

            # Actualizar ventana
            pg.display.update()


# Clase que controla los créditos del juego.
class Creditos:
    """
    Clase que controla los créditos del juego.
    """

    def FuncionCreditos(self):
        # Instancias de las clases
        self.salir = Salir()
        self.main = Main()
        self.boton = Botones()
        self.controles = Controles()

        # Creación de la ventana
        self.ventanaCreditos = Tk()
        self.ventanaCreditos.title("Pong")
        self.ventanaCreditos.resizable(False, False)
        self.ventanaCreditos.config(bg=negro)
        self.ventanaCreditos.iconbitmap("./Images/icono.ico")

        # Centrar ventana
        self.ancho_ventana = 1280
        self.alto_ventana = 720
        self.x_ventana = self.ventanaCreditos.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.ventanaCreditos.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
                str(self.ancho_ventana)
                + "x"
                + str(self.alto_ventana)
                + "+"
                + str(self.x_ventana)
                + "+"
                + str(self.y_ventana)
        )
        self.ventanaCreditos.geometry(self.posicion)

        # Etiquetas
        self.etiquetaCreditos = Etiqueta(
            "Créditos",
            10,
            46,
            azulEtiquetas,
            "Helvetica",
            50,
            self.ventanaCreditos,
        )

        # Autor
        self.etiquetaAutor = Etiqueta(
            "Autor: Raul Catalinas Esteban",
            20,
            23,
            verdeEtiquetas,
            "Helvetica",
            30,
            self.ventanaCreditos,
        )

        # Botones
        self.botonVolverAlMenu = self.boton.BotonPosicionAbsoluta(
            "Volver al menú",
            35,
            30,
            amarilloOscuro,
            lambda: [
                self.ventanaCreditos.destroy(),
                self.main.FuncionMain(),
            ],
            "Helvetica",
            30,
            self.ventanaCreditos,
            amarillo,
            amarilloOscuro,
        )

        self.botonControles = self.boton.BotonPosicionAbsoluta(
            "Controles",
            40,
            30,
            azulOscuro,
            lambda: [
                self.ventanaCreditos.destroy(),
                self.controles.FuncionControles(),
            ],
            "Helvetica",
            30,
            self.ventanaCreditos,
            azul,
            azulOscuro,
        )

        self.botonSalir = self.boton.BotonPosicionAbsoluta(
            "Salir",
            45,
            30,
            rojoOscuro,
            lambda: [
                self.salir.FuncionSalir(self.ventanaCreditos),
            ],
            "Helvetica",
            30,
            self.ventanaCreditos,
            rojo,
            rojoOscuro,
        )

        # Actualizar ventana
        self.ventanaCreditos.mainloop()


# Crear instancia de la clase principal
menu = Main()

# Llamar a la función principal
menu.FuncionMain()
