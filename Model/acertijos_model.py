
class Acertijo:
    def __init__(self, pregunta, respuesta, pista):
        self.pregunta = pregunta
        self.respuesta = respuesta.lower().strip()
        self.pista = pista


def crear_acertijos_basicos():
    """Devuelve la lista de acertijos que usa el juego."""
    acertijos = [

        Acertijo(
            "Se practica sobre dos ruedas y avanza con la fuerza de las piernas. ¿Qué deporte es?",
            "ciclismo",
            "Es un deporte que el profesor Héctor practica mucho."
        ),

        Acertijo(
            "Agua que pasó por aquí, cate que no lo vi. ¿Qué es?",
            "aguacate",
            "Es un juego de palabras."
        ),

        Acertijo(
            "Sube y baja, pero siempre está en el mismo lugar. ¿Qué es?",
            "escalera",
            "Está en edificios o casas."
        ),

        Acertijo(
            "Tiene muchas hojas, pero no es una planta. ¿Qué es?",
            "libro",
            "Lo usas para estudiar."
        ),

        Acertijo(
            "Si hablas, lo rompes. ¿Qué es?",
            "silencio",
            "Necesario para concentrarse."
        ),

        Acertijo(
            "Te muestra todo, pero no dice nada. ¿Qué es?",
            "espejo",
            "Lo usas para arreglarte."
        ),

        Acertijo(
            "Tiene cama pero nunca duerme. ¿Qué es?",
            "rio",
            "Su cama está llena de agua."
        ),

        Acertijo(
            "No tiene vida, pero crece. No respira, pero se muere. ¿Qué es?",
            "fuego",
            "Lo ves en fogatas o estufas."
        ),

        Acertijo(
            "Estoy en el cielo pero no soy avión ni estrella. A veces lloro. ¿Qué soy?",
            "nube",
            "De mí cae la lluvia."
        ),

       
        Acertijo(
            "Tengo muchas llaves pero no abro ninguna puerta. ¿Qué soy?",
            "piano",
            "Se usa para hacer música."
        ),

      
        Acertijo(
            "Tiene dientes pero no come. ¿Qué es?",
            "peine",
            "Lo usas para arreglar tu cabello."
        ),

       
        Acertijo(
            "Corre pero no tiene piernas. ¿Qué es?",
            "agua",
            "Sale por tuberías o ríos."
        ),

      
        Acertijo(
            "Hablo sin boca y escucho sin oídos. ¿Qué soy?",
            "eco",
            "Lo escuchas en montañas."
        ),

       
        Acertijo(
            "Lo puedes romper sin tocarlo. ¿Qué es?",
            "promesa",
            "Es algo que dices, no un objeto."
        ),

     
        Acertijo(
            "Pesa poco, pero si lo metes en un barco, el barco se hunde. ¿Qué es?",
            "agujero",
            "No es un objeto, es una ausencia."
        ),

        
        Acertijo(
            "Está en todas partes, pero no lo puedes ver. ¿Qué es?",
            "aire",
            "Lo respiras."
        ),

        
        Acertijo(
            "Tiene orejas pero no oye. ¿Qué es?",
            "taza",
            "La oreja la usas para agarrarla."
        )
    ]

    return acertijos
