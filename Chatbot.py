# Script de chat simulado en Python utilizando estructuras condicionales

def chat_simulado():
    print("¡Bienvenido al chat simulado!")
    print("Escribe 'salir' para terminar la conversación.\n")

    while True:
        mensaje = input("Tú: ").lower().strip()
        
        if mensaje == 'salir':
            print("ChatBot: ¡Hasta luego!")
            break
        elif mensaje == 'hola':
            print("ChatBot: ¡Hola! ¿Cómo estás?")
        elif mensaje in ['bien, gracias', 'bien', 'muy bien']:
            print("ChatBot: Me alegra saber que estás bien.")
        elif mensaje == 'qué haces':
            print("ChatBot: Estoy aquí, listo para ayudarte en lo que necesites.")
        elif mensaje == 'adiós':
            print("ChatBot: ¡Adiós! Que tengas un excelente día.")
        else:
            print("ChatBot: Lo siento, no entendí tu mensaje. ¿Puedes reformularlo?")

if __name__ == "__main__":
    chat_simulado()
