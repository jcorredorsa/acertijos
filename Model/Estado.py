
import threading


class EstadoJuego:
    def __init__(self, acertijos):
        self.acertijos = acertijos
        self.indice_actual = 0
        self.puntaje = 0

        self.tiempo_restante = 30
        self.pista_disponible = False

        
        self.juego_finalizado = False
        self.rondas_jugadas = 0
        self.rondas_maximas = len(acertijos)

        self.bloqueo = threading.Lock()

    def obtener_acertijo_actual(self):
        if self.juego_finalizado:
            return None
        return self.acertijos[self.indice_actual]

    def pasar_siguiente_acertijo(self):
        """
        Pasa al siguiente acertijo.
        Cuando se han mostrado todos, marca el juego como finalizado.
        """
        self.rondas_jugadas += 1

        if self.rondas_jugadas >= self.rondas_maximas:
            self.juego_finalizado = True
            return

        self.indice_actual = self.rondas_jugadas
        self.tiempo_restante = 30
        self.pista_disponible = False
