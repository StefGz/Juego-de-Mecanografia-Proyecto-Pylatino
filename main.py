import time
from ai import call_gpt
import random

"""
+-----------------------------------------------------------+
| SECCIÓN: PROMPTS PARA GENERAR PALABRAS Y FRASES DEL JUEGO |
+-----------------------------------------------------------+
"""

PROMPT_FACIL = ("""
    Devuelve únicamente una palabra en minúsculas, corta y común, 
    relacionada con alguno de estos temas: {temas}.  
    La palabra debe ser en español y ortográficamente nunca debe llevar tilde. 
    No uses signos de puntuación, números ni caracteres especiales. 
    No repitas ninguna de estas palabras ya usadas: {repetidas}. 
    """)

PROMPT_MEDIO = ("""
    Devuelve únicamente una frase corta en minúsculas, 
    relacionada con alguno de estos temas: {temas}. 
    La frase debe ser en español y natural, contener 3 a 6 palabras, 
    y las palabras principales deben tener longitud media (aproximadamente 4 a 7 letras). 
    Todas las palabras deben ser ortográficamente correctas y nunca llevar tilde.
    No uses signos de puntuación, números ni caracteres especiales. 
    No repitas ninguna de estas palabras o frases ya usadas: {repetidas}.
    Ejemplo de frase correcta: 'correr siempre es divertido'.
    """)

PROMPT_DIFICIL = ("""
    Devuelve únicamente una frase larga en español, 
    relacionada con alguno de estos temas: {temas}.  
    La frase debe ser natural, coherente y contener entre 6 y 10 palabras. 
    Puedes usar mayúsculas, tildes y palabras menos comunes. 
    No uses signos de puntuación, números ni caracteres especiales. 
    Entrega solo la frase sin puntos, comillas ni texto adicional
    No repitas ninguna de estas palabras o frases ya usadas: {repetidas}. 
    Ejemplo de frase correcta: Historias mágicas transforman momentos ordinarios cada día
    """)

PROMPT_AVANZADO = ("""
    Devuelve únicamente una frase compleja en español, 
    relacionada con alguno de estos temas: {temas}.  
    La frase debe ser natural, coherente y contener entre 10 y 15 palabras. 
    La frase debe incluir puntuación obligatoria como comas, puntos, puntos y comas, 
    dos puntos o signos de exclamación e interrogación. 
    La frase debe incluir mayúsculas y palabras complejas o técnicas relacionadas con los temas avanzados, 
    como términos científicos, artísticos o especializados. 
    Puedes usar signos especiales como comillas, paréntesis o guiones si el contexto lo requiere.
    Varía la estructura de cada frase, alternando entre oraciones descriptivas, exclamativas, 
    interrogativas o comparativas, y cambiando el orden de sujeto, acción y descripción.
    No repitas ninguna de estas palabras o frases ya usadas: {repetidas}. 
    Ejemplo de frase correcta: La sinfonía barroca, ejecutada con contrapunto y polifonía, 
    despierta emociones profundas en los oyentes más exigentes.
    """)

#Recibe una plantilla de un prompt para formatearla y devolver su versión final
def generar_prompt(plantilla_prompt, lista_temas, contenido_generado):
    temas_seleccionados = ", ".join(lista_temas)
    contenido_repetido = ", ".join(contenido_generado)

    return plantilla_prompt.format(temas = temas_seleccionados, repetidas = contenido_repetido)

"""
+-------------------------------+
| SECCIÓN: DIFICULTAD DEL JUEGO |
+-------------------------------+
"""

#Retorna la dificultad seleccionada con su respectivo prompt
def preparar_dificultad():
    plantilla_seleccionada = ""

    dificultad_seleccionada = seleccionar_dificultad()

    if dificultad_seleccionada == 1:
        plantilla_seleccionada = PROMPT_FACIL
    elif dificultad_seleccionada == 2:
        plantilla_seleccionada = PROMPT_MEDIO
    elif dificultad_seleccionada == 3:
        plantilla_seleccionada = PROMPT_DIFICIL
    elif dificultad_seleccionada == 4:
        plantilla_seleccionada = PROMPT_AVANZADO

    if plantilla_seleccionada != "":
        print("""
✅​ Dificultad agregada con éxito.
""")
        dibujar_linea_separadora()
        pausa()

        return plantilla_seleccionada

#Permite al usuario elegir la dificultad o regresar menú principal
def seleccionar_dificultad():
    mostrar_menu_dificultad()

    entrada_usuario = input("""
​👉​ Ingresa el número correspondiente a tu selección o presiona 
cualquier tecla si quieres volver al menú principal: """)

    print(" ")

    if not entrada_usuario or not entrada_usuario.isdigit():
        return 0

    numero_dificultad = int(entrada_usuario)

    if numero_dificultad <= 4 and numero_dificultad >= 1:
        return numero_dificultad
    else:
        return 0

"""
+-------------------------------------------------------------+
| SECCIÓN: MENSAJES DE INFORMACIÓN (MENÚ, INSTRUCCIONES, ETC) |
+-------------------------------------------------------------+
"""
#Simula un efecto de pausa
def pausa():
    time.sleep(1)

#Dibuja una línea para separar apartados durante la ejecución del juego
def dibujar_linea_separadora():
    print("   "+ "+" + "-" * 60 + "+")

#Muestra el mensaje de bienvenida inicial
def mostrar_bienvenida():
    dibujar_linea_separadora()
    print("   |       ⌨️ ¡Bienvenido/a al Juego de Mecanografía! ⌨️       |")
    dibujar_linea_separadora()

#Muestra el menú principal del programa
def mostrar_menu_principal():
    pausa()

    menu_opciones = """ 
🔹​ Por favor, selecciona una de las siguientes opciones:

1. Leer instrucciones del juego.
2. Iniciar la partida.
3. Ingresar temas.
4. Escoger la dificultad del juego.
5. Escoger el modo de juego.
6. Salir del juego.""" 

    print(menu_opciones)
    dibujar_linea_separadora()
    pausa()

#Muestra el menú de dificultad de la partida
def mostrar_menu_dificultad():
    pausa()

    menu_opciones = """ 
🔹​ Selecciona la dificultad en la que deseas jugar:

1. Fácil (Palabras comunes y cortas)
2. Medio (Frases cortas con palabras de longitud media)
3. Difícil (Frases más largas, mayúsculas, palabras con tildes y menos comunes)
4. Avanzado (Frases con puntuación y temas específicos complejos)
""" 
    print(menu_opciones)
    dibujar_linea_separadora()
    pausa()

#Muestra el menú de modo de juego
def mostrar_modos_juego():
    pausa()

    menu_opciones = """ 
🔹​ Selecciona el modo en que deseas jugar:

1. Práctica (Solo palabras y frases sin temporizador)
2. Competición (Contador de vidas y desafíos ocasionales)
"""
    print(menu_opciones)
    dibujar_linea_separadora()
    pausa()

#Muestra las instrucciones del juego
def mostrar_instru_juego():
    pausa()

    instrucciones = """
📃​ Instrucciones de juego 📃​
    
¡Bienvenido/a! pon a prueba tu habilidad de escritura en el teclado de forma divertida.

​🟢​ ¿Cómo Jugar?

​1. Elige tu configuración: Antes de iniciar, deberás seleccionar el modo de juego, la dificultad 
y los temas bases a incluir en la partida.

2. Escribe la palabra o frase: Cada frase nueva es una ronda. Tu objetivo es escribirla 
exactamente como aparece. 

3. Desafíos: En el modo competición hay una probabilidad de que aparezca un desafío, en donde 
las palabras o frases se deben escribir en reversa, presta atención a este detalle.

🔴 Reglas de fallos (Modo competición):

1. Tienes un máximo de 5 vidas en fácil/medio y un máximo de 3 vidas en difícil/avanzado.
2. Si el contador de vidas llega a 0, la partida termina inmediatamente. 
3. Si decides jugar de nuevo, el contador de vidas se restablece.

⚠️​ ADVERTENCIA: 

1. En los niveles fácil y medio intentamos que todas las palabras y frases estén libres de tildes 
y signos. Aun así, en raras ocasiones podría aparecer alguno accidentalmente.

2.En frases largas, la limitación del ancho de la consola puede cortar una palabra entre líneas; 
Lee siempre la línea siguiente para teclear la palabra completa.


¡Mucha suerte y a escribir! ⌨️ """

    print(instrucciones)
    dibujar_linea_separadora()

    input("""
​👉​​​​ Presiona cualquier tecla para regresar al menú principal: """)

    print(" ")
    dibujar_linea_separadora()
    pausa()
    
"""
+------------------------------+
| SECCION: TEMAS DE LA PARTIDA |
+------------------------------+
"""
#Crea una lista de temas que se usara en el juego, a partir de lo que ingrese el usuario
def preparar_lista_temas():
    temas = []

    pausa()
    
    instruccion = """
​👉​​ Ingresa uno o varios temas para generar las palabras y 
frases de la partida. Si quieres volver al menú principal, 
presiona enter.
"""
    print(instruccion)
    dibujar_linea_separadora()

    while True:
        entrada_tema = input("""
Ingresa el tema de tu preferencia o presiona enter: """)
        print(" ")
        
        if entrada_tema:
            temas.append(entrada_tema.lower())
            print("""
✅​ Tema guardado con éxito.""")  
            dibujar_linea_separadora()
        else:
            break

    dibujar_linea_separadora()
    pausa()

    return(temas)

"""
+-------------------------+
| SECCIÓN: MENÚ DEL JUEGO |
+-------------------------+
"""

#Solicita al usuario seleccionar una de las opciones del menú
def seleccionar_opcion_menu():
    mostrar_menu_principal()

    entrada_usuario = input("""
​👉​ Ingresa el número correspondiente a tu selección: """)

    print(" ")
    dibujar_linea_separadora()

    return entrada_usuario

#Valida la selección del usuario respecto al menú principal
def validar_seleccion_menu():
    while True:
        seleccion_usuario = seleccionar_opcion_menu()

        if not seleccion_usuario or not seleccion_usuario.isdigit():
            print("""
❌​ Opción incorrecta, por favor ingresa un número válido.""")   
            continue

        numero_seleccion = int(seleccion_usuario)

        if numero_seleccion > 6 or numero_seleccion < 1:
            print("""
❌​ Opción incorrecta, por favor ingresa un número válido.""")    
            continue

        return numero_seleccion

"""
+------------------------+
| SECCIÓN: MODO DE JUEGO |
+------------------------+
"""
#Permite al usuario elegir el modo de juego o regresar menú principal
def seleccionar_modo_juego():
    mostrar_modos_juego()

    entrada_usuario = input("""
​👉​ Ingresa el número correspondiente a tu selección o presiona 
cualquier tecla si quieres volver al menú principal: """)
    print(" ")

    if not entrada_usuario or not entrada_usuario.isdigit():
        return 0

    numero_modo_juego = int(entrada_usuario)

    if numero_modo_juego <= 2 and numero_modo_juego >= 1:
        print("""
✅​ Modo de juego agregado con éxito.
""")
        dibujar_linea_separadora()
        pausa()
        return numero_modo_juego
    else:
        return 0

#Ejecuta el juego en modo práctica
def modo_practica(prompt, lista_temas, contenido_generado):
    print("""
👉 Escribe "salir" en el momento en que desees terminar la partida 
y volver al menú principal.
""")

    while True:
        prompt_generado = generar_prompt(prompt, lista_temas, contenido_generado)

        print("""
💬​ Generando nueva palabra o frase...
""")
        ronda = call_gpt(prompt_generado)
        contenido_generado.append(ronda)
        print(f"​    ➡️​ {ronda}")

        rta_usuario = input("""
👉 Escribe la palabra o frase: """)  

        if rta_usuario.lower() == "salir":
            break

        if ronda == rta_usuario:
            print("""
✔️​​ ¡Correcto!
""")
            dibujar_linea_separadora()
        else:
            print("""
❌​ ¡Incorrecto!
""")
            dibujar_linea_separadora()

#Ejecuta el juego en modo competición
def modo_competicion(prompt, lista_temas, contenido_generado):
    rondas_ganadas = 0
    vidas = 0

    if prompt == PROMPT_FACIL or prompt == PROMPT_MEDIO:
        vidas = 5
    else:
        vidas = 3

    print("""
👉 Escribe "salir" en el momento en que desees terminar la partida 
y volver al menú principal.
""")

    print(f"""
❤️​ Vidas iniciales: {vidas}
""")
    dibujar_linea_separadora()

    while vidas > 0:
        prompt_generado = generar_prompt(prompt, lista_temas, contenido_generado)

        print("""
💬​ Generando nueva palabra o frase...
""")    
        desafio = random.randint(1, 100)
        ronda = call_gpt(prompt_generado)
        contenido_generado.append(ronda)

        if desafio <= 20:
            frase_reversa = ronda[::-1]
            ronda = frase_reversa
        
        print(f"​    ➡️​ {ronda}")

        rta_usuario = input("""
👉 Escribe la palabra o frase: """)   
 
        if rta_usuario.lower() == "salir":
            break

        if ronda == rta_usuario:
            rondas_ganadas +=1
            print("""
✔️​​ ¡Correcto!
""")
            dibujar_linea_separadora()
        else:
            print("""
❌​ ¡Incorrecto!
""")        
            vidas -=1
            print(f"""
❤️​ Vidas restantes: {vidas}
""")
            dibujar_linea_separadora()

    print(f"""
​🏆​​ Total de rondas ganadas en esta partida: {rondas_ganadas}
""")    
    dibujar_linea_separadora()

"""
+------------------------------+
| SECCIÓN: EJECUCION DEL JUEGO |
+------------------------------+
"""

#Inicia el juego
def iniciar_juego(): 
    temas_partida = []
    contenido_generado = []
    prompt_dificultad = ""
    modo_juego = ""

    mostrar_bienvenida()

    while True:
        entrada_menu = validar_seleccion_menu()

        if entrada_menu == 1:
            mostrar_instru_juego()
        elif entrada_menu == 2:
            if not temas_partida:
                print("""
⚠️​ Debes ingresar minimo un tema para poder jugar.
""")        
            elif prompt_dificultad == "":
                print("""
⚠️​ Debes elegir una la dificultad de la partida.
""")        
            elif modo_juego == "":
                print("""
⚠️​ Debes elegir el modo de juego.
""")        
            else:
                if modo_juego == 1:
                    modo_practica(prompt_dificultad, temas_partida, contenido_generado)
                elif modo_juego == 2:
                    modo_competicion(prompt_dificultad, temas_partida, contenido_generado)
        elif entrada_menu == 3:
            nuevos_temas = preparar_lista_temas()
            if nuevos_temas:
                temas_partida = nuevos_temas
        elif entrada_menu == 4:
            nueva_dificultad = preparar_dificultad()
            if nueva_dificultad is not None:
                prompt_dificultad = nueva_dificultad
        elif entrada_menu == 5:
            nuevo_modo = seleccionar_modo_juego()
            if nuevo_modo != 0:
                modo_juego = nuevo_modo
        elif entrada_menu == 6:
            pausa()
            print("""
​¡Gracias por jugar, que tengas un lindo día!🤗
            ​""")
            dibujar_linea_separadora()
            break
        
def main():
    iniciar_juego()

if __name__ == "__main__":
    main()
