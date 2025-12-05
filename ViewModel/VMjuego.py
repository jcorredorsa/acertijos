# viewmodel/vista_modelo_juego.py
import threading
import time


class VistaModeloJuego:
    def __init__(self, estado_juego):
        self.estado = estado_juego
        self.jugando = False

        self.hilo_temporizador = None
        self.hilo_pista = None

        # Bandera para avisar a la vista que se acabó el tiempo
        self.mensaje_tiempo_agotado = False

    # ---------- Métodos para que la Vista consulte datos ----------
    def obtener_pregunta_actual(self):
        if self.estado.juego_finalizado:
            return "El juego ha terminado."
        acertijo = self.estado.obtener_acertijo_actual()
        if acertijo is None:
            return "El juego ha terminado."
        return acertijo.pregunta

    def obtener_puntaje(self):
        return self.estado.puntaje

    def obtener_tiempo_restante(self):
        with self.estado.bloqueo:
            return self.estado.tiempo_restante

    def pista_esta_disponible(self):
        with self.estado.bloqueo:
            return self.estado.pista_disponible

    def obtener_texto_pista(self):
        acertijo = self.estado.obtener_acertijo_actual()
        if acertijo is None:
            return ""
        return acertijo.pista

    def juego_ha_terminado(self):
        return self.estado.juego_finalizado

    
    def iniciar_juego(self):
        self.jugando = True
        self._iniciar_hilos()

    def detener_juego(self):
        self.jugando = False

    def verificar_respuesta(self, respuesta_usuario):
        if self.estado.juego_finalizado:
            return "El juego ya terminó."

        acertijo_actual = self.estado.obtener_acertijo_actual()
        if acertijo_actual is None:
            return "El juego ya terminó."

        respuesta_correcta = acertijo_actual.respuesta
        respuesta_usuario = respuesta_usuario.lower().strip()

        with self.estado.bloqueo:
            if respuesta_usuario == respuesta_correcta:
                self.estado.puntaje += 1
                mensaje = "Correcto."
            else:
                mensaje = f"Incorrecto. La respuesta era: {respuesta_correcta}"

            # Pasamos al siguiente acertijo (o terminamos el juego)
            self.estado.pasar_siguiente_acertijo()

        return mensaje

    def saltar_acertijo(self):
        """Pasa al siguiente acertijo sin cambiar el puntaje."""
        with self.estado.bloqueo:
            if not self.estado.juego_finalizado:
                self.estado.pasar_siguiente_acertijo()

    # ---------- Manejo de hilos ----------
    def _iniciar_hilos(self):
        # Hilo 1: temporizador
        self.hilo_temporizador = threading.Thread(
            target=self._bucle_temporizador,
            daemon=True
        )
        # Hilo 2: habilitar pista
        self.hilo_pista = threading.Thread(
            target=self._bucle_pista,
            daemon=True
        )

        self.hilo_temporizador.start()
        self.hilo_pista.start()

    def _bucle_temporizador(self):
        """Hilo que descuenta el tiempo y cambia de acertijo cuando llega a 0."""
        while self.jugando:
            time.sleep(1)
            with self.estado.bloqueo:

                if self.estado.juego_finalizado:
                    self.jugando = False
                    break

                self.estado.tiempo_restante -= 1

                # Cuando se acaban los segundos
                if self.estado.tiempo_restante <= 0:
                    # Avisamos a la vista para que muestre el mensaje
                    self.mensaje_tiempo_agotado = True

                    # Pasamos al siguiente acertijo (o terminamos)
                    self.estado.pasar_siguiente_acertijo()

                    if self.estado.juego_finalizado:
                        self.jugando = False
                        break

    def _bucle_pista(self):
        """
        Hilo que activa la pista después de unos segundos
        para cada acertijo.
        """
        segundos_para_pista = 5  # puedes cambiar a 10 si quieres más tiempo
        contador = 0
        ultimo_indice = self.estado.indice_actual

        while self.jugando:
            time.sleep(1)
            with self.estado.bloqueo:

                if self.estado.juego_finalizado:
                    self.jugando = False
                    break

                # Si cambiamos de acertijo, reiniciamos contador y bloqueamos la pista
                if self.estado.indice_actual != ultimo_indice:
                    ultimo_indice = self.estado.indice_actual
                    contador = 0
                    self.estado.pista_disponible = False

                # Si aún no hay pista disponible, vamos contando
                if not self.estado.pista_disponible:
                    contador += 1
                    if contador >= segundos_para_pista:
                        self.estado.pista_disponible = True
