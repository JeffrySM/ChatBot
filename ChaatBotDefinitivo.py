import nltk
import tkinter as tk
#from tkinter import scrolledtex
from tkinter import PhotoImage




from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

# Definimos algunos pares de preguntas y respuestas
pares = [
    [
        r"(Hola|Hola!|Hola|Saludos)",
        ["¡Hola! ¿En qué puedo ayudarte?", "Hola, ¿cómo puedo asistirte hoy?"]
    ],
    [
        r"(¿Cómo estás?|¿Qué tal?|¿Cómo te va?)",
        ["Soy un chatbot, así que siempre estoy listo para ayudar.", "Estoy bien, gracias. ¿En qué puedo ayudarte?"]
    ],
    [
        r"(Adiós|Hasta luego|Chao)",
        ["Hasta luego. Si tienes más preguntas, no dudes en preguntar.", "Adiós. ¡Ten un buen día!"]
    ],
    [
        r"(¿Quién eres?|¿Qué eres?)",
        ["Soy un chatbot creado en Python. Estoy diseñado para responder preguntas y ayudarte con información."]
    ],
    [
        r"(Gracias|Gracias por tu ayuda)",
        ["De nada, ¡estoy aquí para ayudar!"]
    ],
    # Nuevos pares de preguntas y respuestas médicas
    [
        r"(¿Puedes darme información médica?|Necesito consejos médicos)",
        ["Lamento, no soy un profesional médico, pero puedo proporcionarte información general. ¿En qué área médica necesitas ayuda?"]
    ],
    [
        r"(¿Cómo prevenir resfriados?|¿Qué debo hacer si tengo fiebre?)",
        ["Para obtener consejos médicos específicos, te recomendamos consultar a un profesional de la salud."]
    ],
    [
        r"(¿Qué debo hacer en caso de una emergencia médica?|¿Cómo realizar RCP?)",
        ["En caso de una emergencia médica, llama al número de emergencia de tu país. Aprender RCP (reanimación cardiopulmonar) es útil; sin embargo, te aconsejo que tomes un curso oficial para aprender técnicas adecuadas."]
    ],
    [
        r"(¿Dónde puedo encontrar un médico cerca de mí?|¿Conoces un buen médico?)",
        ["Puedes buscar un médico cerca de ti en línea a través de sitios web de salud o preguntar a amigos y familiares para obtener recomendaciones."]
    ],
    [
        r"(¿Cuáles son los síntomas del COVID-19?|¿Cómo puedo protegerme del COVID-19?)",
        ["Los síntomas comunes del COVID-19 incluyen fiebre, tos, dificultad para respirar y pérdida del olfato o el gusto. Para protegerte, sigue las pautas de prevención de tu autoridad de salud local, como usar mascarilla y practicar el distanciamiento social."]
    ],
    [
        r"(¿Qué debo hacer si tengo alergias estacionales?|¿Cómo aliviar la congestión nasal?)",
        ["Para aliviar las alergias estacionales, consulta a un alergólogo. Puedes probar antihistamínicos de venta libre y evitar el contacto con alérgenos conocidos."]
    ],
    [
        r"(¿Cuáles son las mejores prácticas de higiene personal?|¿Cómo debo lavarme las manos correctamente?)",
        ["Las mejores prácticas de higiene incluyen lavarse las manos regularmente durante al menos 20 segundos con agua y jabón, y cubrirse la boca y la nariz al toser o estornudar."]
    ],
    [
        r"(¿Dónde puedo encontrar información confiable sobre salud?|¿Qué sitios web recomiendas para información médica?)",
        ["Sitios web confiables para obtener información médica incluyen WebMD, MedlinePlus y los sitios web de instituciones de salud como la OMS y los CDC."]
    ],
    [
        r"(¿Cuáles son los beneficios del ejercicio?|¿Cuánto ejercicio se recomienda a diario?)",
        ["El ejercicio regular tiene numerosos beneficios para la salud, incluyendo la mejora de la condición cardiovascular y la reducción del estrés. Se recomienda al menos 150 minutos de actividad física moderada a la semana."]
    ],
    
     [
        r"(¿Cuál es el impacto del cambio climático en la biodiversidad?|¿Cómo afecta el cambio climático a la biodiversidad?)",
        ["El cambio climático afecta la biodiversidad al alterar los patrones climáticos, resultando en la pérdida de hábitats y cambios en los ciclos de reproducción de las especies."]
    ],
    [
        r"(¿Cómo funciona la tecnología blockchain y cuáles son sus aplicaciones más allá de las criptomonedas?|Explícame la tecnología blockchain y sus usos fuera de las criptomonedas)",
        ["La tecnología blockchain es un sistema de registro descentralizado y seguro. Se utiliza en contratos inteligentes, seguimiento de la cadena de suministro, voto electrónico y más, debido a su transparencia y seguridad."]
    ],
    [
        r"(¿Cuáles son los desafíos éticos en la inteligencia artificial?|Háblame sobre los problemas éticos en la inteligencia artificial)",
        ["Los desafíos éticos en la inteligencia artificial incluyen privacidad, sesgo algorítmico, toma de decisiones autónoma, impacto en el empleo y responsabilidad en caso de errores."]
    ],
    [
        r"(¿Cuáles son las teorías actuales sobre el origen del universo?|Explícame las teorías sobre el origen del universo)",
        ["Las teorías incluyen el Big Bang, la teoría de cuerdas y la inflación cósmica, que buscan explicar eventos desde el inicio del universo."]
    ],
    [
        r"(¿Explícame el concepto de singularidad tecnológica?|¿Qué es la singularidad tecnológica?)",
        ["La singularidad tecnológica es la hipotética llegada de un punto en el futuro donde el progreso tecnológico se acelera exponencialmente, llevando a cambios drásticos e incontrolables en la sociedad debido a la superinteligencia artificial."]
    ],
    [
        r"(¿Cuáles son las principales teorías éticas en filosofía moral?|Háblame sobre las teorías éticas en filosofía moral)",
        ["Incluyen el utilitarismo, la deontología y la ética de la virtud, que se centran en maximizar la felicidad, cumplir con deberes y desarrollar virtudes personales, respectivamente."]
    ],
    [
        r"(¿Cómo se forman los agujeros negros y cuál es su papel en el cosmos?|Explícame la formación de los agujeros negros y su función cósmica)",
        ["Los agujeros negros se forman por el colapso gravitacional de estrellas masivas. Tienen una fuerza gravitatoria tan intensa que nada, ni siquiera la luz, puede escapar. Desempeñan un papel crucial en la estructura y evolución del universo."]
    ],
    [
        r"(¿Cuáles son las implicaciones de la realidad aumentada en la educación?|Explícame cómo la realidad aumentada afecta a la educación)",
        ["La realidad aumentada en la educación mejora la interactividad, permite la visualización tridimensional de conceptos y ofrece experiencias inmersivas, mejorando la retención y comprensión del material."]
    ],

]
# Creamos el chatbot
chatbot = Chat(pares, reflections)






# Función para enviar un mensaje al chatbot y mostrar la respuesta
def enviar_mensaje():
    mensaje_usuario = entrada_usuario.get()
    respuesta = chatbot.respond(mensaje_usuario)
    conversacion.config(state='normal')
    conversacion.insert(tk.END, "Tú: " + mensaje_usuario + "\n")
    conversacion.insert(tk.END, "Chatbot: " + respuesta + "\n")
    conversacion.config(state='disabled')
    entrada_usuario.delete(0, tk.END)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("ChatterBuddy ")
ventana.geometry("400x400")
ventana.configure(bg='#00CED1')

# Configuración de la conversación
conversacion = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
conversacion.insert(tk.END, "Chatbot: ¡Hola! ¿En qué puedo ayudarte?\n")
conversacion.config(state='disabled',bg='#A9A9A9')
conversacion.pack()


# Campo de entrada de texto
entrada_usuario = tk.Entry(ventana, width=30)
entrada_usuario.pack()

# Botón para enviar el mensaje
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje,bg='#4CAF50', fg='#FFFFFF')
boton_enviar.pack()

#Agregar un logo a la ventana


logo_label = tk.Label(ventana, image=logo_image, bg='#D3D3D3')
logo_label.pack()
#Mostrar la imagen en un widget Label y colocarlo en la esquina superior izquierda



# Ejecutar la interfaz gráfica
ventana.mainloop()




pares = [
    [
        r"(Hola|Hola!|Hola|Saludos)",
        ["¡Hola! ¿En qué puedo ayudarte?", "Hola, ¿cómo puedo asistirte hoy?"]
    ],
    [
        r"(¿Cómo estás?|¿Qué tal?|¿Cómo te va?)",
        ["Soy un chatbot, así que siempre estoy listo para ayudar.", "Estoy bien, gracias. ¿En qué puedo ayudarte?"]
    ],
    [
        r"(Adiós|Hasta luego|Chao)",
        ["Hasta luego. Si tienes más preguntas, no dudes en preguntar.", "Adiós. ¡Ten un buen día!"]
    ],
    [
        r"(¿Quién eres?|¿Qué eres?)",
        ["Soy un chatbot creado en Python. Estoy diseñado para responder preguntas y ayudarte con información."]
    ],
    [
        r"(Gracias|Gracias por tu ayuda)",
        ["De nada, ¡estoy aquí para ayudar!"]
    ],
    # Nuevos pares de preguntas y respuestas médicas
    [
        r"(¿Puedes darme información médica?|Necesito consejos médicos)",
        ["Lamento, no soy un profesional médico, pero puedo proporcionarte información general. ¿En qué área médica necesitas ayuda?"]
    ],
    [
        r"(¿Cómo prevenir resfriados?|¿Qué debo hacer si tengo fiebre?)",
        ["Para obtener consejos médicos específicos, te recomendamos consultar a un profesional de la salud."]
    ],
    [
        r"(¿Qué debo hacer en caso de una emergencia médica?|¿Cómo realizar RCP?)",
        ["En caso de una emergencia médica, llama al número de emergencia de tu país. Aprender RCP (reanimación cardiopulmonar) es útil; sin embargo, te aconsejo que tomes un curso oficial para aprender técnicas adecuadas."]
    ],
    [
        r"(¿Dónde puedo encontrar un médico cerca de mí?|¿Conoces un buen médico?)",
        ["Puedes buscar un médico cerca de ti en línea a través de sitios web de salud o preguntar a amigos y familiares para obtener recomendaciones."]
    ],
    [
        r"(¿Cuáles son los síntomas del COVID-19?|¿Cómo puedo protegerme del COVID-19?)",
        ["Los síntomas comunes del COVID-19 incluyen fiebre, tos, dificultad para respirar y pérdida del olfato o el gusto. Para protegerte, sigue las pautas de prevención de tu autoridad de salud local, como usar mascarilla y practicar el distanciamiento social."]
    ],
    [
        r"(¿Qué debo hacer si tengo alergias estacionales?|¿Cómo aliviar la congestión nasal?)",
        ["Para aliviar las alergias estacionales, consulta a un alergólogo. Puedes probar antihistamínicos de venta libre y evitar el contacto con alérgenos conocidos."]
    ],
    [
        r"(¿Cuáles son las mejores prácticas de higiene personal?|¿Cómo debo lavarme las manos correctamente?)",
        ["Las mejores prácticas de higiene incluyen lavarse las manos regularmente durante al menos 20 segundos con agua y jabón, y cubrirse la boca y la nariz al toser o estornudar."]
    ],
    [
        r"(¿Dónde puedo encontrar información confiable sobre salud?|¿Qué sitios web recomiendas para información médica?)",
        ["Sitios web confiables para obtener información médica incluyen WebMD, MedlinePlus y los sitios web de instituciones de salud como la OMS y los CDC."]
    ],
    [
        r"(¿Cuáles son los beneficios del ejercicio?|¿Cuánto ejercicio se recomienda a diario?)",
        ["El ejercicio regular tiene numerosos beneficios para la salud, incluyendo la mejora de la condición cardiovascular y la reducción del estrés. Se recomienda al menos 150 minutos de actividad física moderada a la semana."]
    ],
]





    
# Creamos el chatbot y lo inicializamos
chatbot = Chat(pares, reflections)
print("Hola, soy un chatbot. Puedes escribir 'salir' para terminar la conversación.")
chatbot.converse()
