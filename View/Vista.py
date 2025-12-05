
import tkinter as tk
from tkinter import messagebox


class VistaPrincipal:
    def __init__(self, raiz, vista_modelo):
        self.raiz = raiz
        self.vm = vista_modelo

        self.raiz.title("Juego de Acertijos")
        self.raiz.geometry("500x300")

        self.juego_terminado_mostrado = False

        
        self.etiqueta_pregunta = tk.Label(
            self.raiz,
            text="Pregunta",
            wraplength=450,
            font=("Arial", 12)
        )
        self.etiqueta_pregunta.pack(pady=10)

        
        self.entrada_respuesta = tk.Entry(self.raiz, font=("Arial", 12))
        self.entrada_respuesta.pack(pady=5)

     
        self.marco_botones = tk.Frame(self.raiz)
        self.marco_botones.pack(pady=5)

        self.boton_responder = tk.Button(
            self.marco_botones,
            text="Responder",
            command=self.al_presionar_responder
        )
        self.boton_responder.grid(row=0, column=0, padx=5)

        self.boton_siguiente = tk.Button(
            self.marco_botones,
            text="Siguiente",
            command=self.al_presionar_siguiente
        )
        self.boton_siguiente.grid(row=0, column=1, padx=5)

        self.boton_pista = tk.Button(
            self.marco_botones,
            text="Ver pista",
            state=tk.DISABLED,
            command=self.al_presionar_pista
        )
        self.boton_pista.grid(row=0, column=2, padx=5)

        
        self.marco_info = tk.Frame(self.raiz)
        self.marco_info.pack(pady=10)

        self.etiqueta_puntaje = tk.Label(self.marco_info, text="Puntaje: 0")
        self.etiqueta_puntaje.grid(row=0, column=0, padx=10)

        self.etiqueta_tiempo = tk.Label(self.marco_info, text="Tiempo: 30 s")
        self.etiqueta_tiempo.grid(row=0, column=1, padx=10)

        
        self.actualizar_pregunta()
        self.vm.iniciar_juego()

       
        self.actualizar_interfaz()

       
        self.raiz.protocol("WM_DELETE_WINDOW", self.al_cerrar_ventana)

    
    def al_presionar_responder(self):
        texto_usuario = self.entrada_respuesta.get()
        if not texto_usuario.strip():
            messagebox.showinfo("Aviso", "Escribe una respuesta.")
            return

        resultado = self.vm.verificar_respuesta(texto_usuario)
        messagebox.showinfo("Resultado", resultado)

        self.entrada_respuesta.delete(0, tk.END)
        self.actualizar_pregunta()

    def al_presionar_siguiente(self):
        self.vm.saltar_acertijo()
        self.entrada_respuesta.delete(0, tk.END)
        self.actualizar_pregunta()
        messagebox.showinfo("Siguiente", "Pasaste al siguiente acertijo.")

    def al_presionar_pista(self):
        texto_pista = self.vm.obtener_texto_pista()
        if texto_pista:
            messagebox.showinfo("Pista", texto_pista)

    def al_cerrar_ventana(self):
        self.vm.detener_juego()
        self.raiz.destroy()

    
    def actualizar_pregunta(self):
        self.etiqueta_pregunta.config(text=self.vm.obtener_pregunta_actual())
        self.etiqueta_puntaje.config(text=f"Puntaje: {self.vm.obtener_puntaje()}")

    def actualizar_interfaz(self):
        
        if getattr(self.vm, "mensaje_tiempo_agotado", False):
            self.vm.mensaje_tiempo_agotado = False
            messagebox.showinfo(
                "Tiempo agotado",
                "Se acabó el tiempo. Pasando al siguiente acertijo."
            )
            self.entrada_respuesta.delete(0, tk.END)
            self.actualizar_pregunta()

        if self.vm.juego_ha_terminado():
            if not self.juego_terminado_mostrado:
                self.juego_terminado_mostrado = True
                messagebox.showinfo(
                    "Fin del juego",
                    f"El juego ha terminado.\nPuntaje final: {self.vm.obtener_puntaje()}"
                )
                self.al_cerrar_ventana()
            return

        
        tiempo = self.vm.obtener_tiempo_restante()
        self.etiqueta_tiempo.config(text=f"Tiempo: {tiempo} s")

    
        self.etiqueta_puntaje.config(text=f"Puntaje: {self.vm.obtener_puntaje()}")

       
        if self.vm.pista_esta_disponible():
            self.boton_pista.config(state=tk.NORMAL)
        else:
            self.boton_pista.config(state=tk.DISABLED)

       
        self.raiz.after(200, self.actualizar_interfaz)
