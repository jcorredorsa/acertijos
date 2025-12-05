
import tkinter as tk

from Model.acertijos_model import crear_acertijos_basicos
from Model.Estado import EstadoJuego
from ViewModel.VMjuego import VistaModeloJuego
from View.Vista import VistaPrincipal


def main():
    acertijos = crear_acertijos_basicos()
    estado = EstadoJuego(acertijos)
    vista_modelo = VistaModeloJuego(estado)

    raiz = tk.Tk()
    app = VistaPrincipal(raiz, vista_modelo)
    raiz.mainloop()


if __name__ == "__main__":
    main()
