label inicio:
    show screen _music
    if persistent.console_:
        menu:
            "Deseas comenzar desde el principio o quieres que conversermos acerca de las variables"
            "Desde el principio: Recuerda que la consola del desarrollador está activa":
                jump inicio_
            "Deseo conocer más acerca de las variables":
                jump console_
    elif persistent.console is not None:
        $ persistent.console=False
        $ persistent.console_=False
label inicio_:
    $ now_playing=musica[:-4]
    #textbutton "Music" action Show("_music") 
    show gopher_logo at truecenter
    show text "{color=#000000}Logo de Go: Gopher{/color}" at subtitle
    h "Hola nuevamente, me llamo Hedley"
    h "Soy un médico gradudado de la Universidad de Panamá, tengo una maestría en Biología molecular y estoy estudiando un doctorado en epidemiología en el Instituto Karolinska"
    h "En esta ocasión les voy a mostrar ciertas cositas fundamentales del lenguaje Go."
    h "El lenguaje Go es bastante nuevo, en comparación con la enorme familia C (C, Objective C, C++ o C#), Python, Java, JavaScript, etc"
    h "Sin embargo, la idea de este lenguaje, es al igual que otro llamado Swift, el de proveer las mejorar ciertos aspectos de sus predecesores."
    h "La gran ventaja de Go es que este puede correr en múltiples procesos simultáneamente"

    $info = True
    h "En la esquina superior derecha, veras un botón que muestra u oculta una serie de enlaces útiles"
    h "Estos enlaces son la página oficial del lenguaje Go, la página de la Wikipedia, el parque recreativo de Go y mi jarrón de propinas de PayPal por si quieres cooperar conmigo"
    h "Vamos a empezar..."
    h "La sección siguiente trata de principios básicos de programación"
    h "Es muy similar a lo que mostré en mi aplicación para aprender Python"
    h "Puede adquirir la aplicación para aprender Python {a=https://play.google.com/store/apps/details?id=com.hedleypanama}aqui{/a}"
    hide gopher_logo at truecenter
    menu:
        "Si lo deseas, puedes saltarte esta parte y entrar de lleno a aprender Go\nPero no te recomiendo hacerlo si nunca has programado\n¿Qué deseas hacer?"
        "Deseo conocer los principios básicos de programación":
            pass
        "Deseo entrar de lleno a aprender Go":
            jump Go_1
    #hide text
    jump chp1
label chp1:
    show gopher_logo
    show text "{size=40}{color=#000}Capítulo uno\n\n\n¿Qué es programar?{/color}{/size}" at top
    h "Para mi, aprender a programar me pareció bastante frustrante!"
    h "Verán, aprendí varios lenguajes de programación, pero no supe lo que era programar..."
    h "Vamos a intentar aprender a programar antes de entrar de lleno a Go"
    h "Vamos a iniciar con el concepto del {color=#ff0}proyecto{/color}"
    h "Los {color=#ff0}proyectos{/color} están asociados a 2 conceptos:"
    h 'El primero es que el proyecto debe tener la finalidad de {color=#ff0}resolver un problema{/color}'
    h 'El {color=#ff0}problema{/color} es de caracter repetitivo y se resuelve mediante la {color=#ff0}interacción{/color} de partes de un {color=#ff0}sistema{/color}'
    h "El {color=#ff0}sistema{/color} es el segundo concepto"
    h "Las partes del sistema están contenidas en una {color=ff0}carpeta{/color} o un {color=#ff0}directorio{/color} dentro de la {color=#ff0}computadora{/color} (llamado en España{color=#ff0}\"ordernador\"{/color}) o en la {color=#ff0}nube{/color}"
    
    $current="q1"
    $ error=""
    
    label q1:
        if error != "":
            h "{color=#f00}[error]{/color}"
        hide gopher_logo
        menu:
            "¿Cuál de los siguientes conceptos están asociados al concepto del proyecto"
            "Un perro":
                $error="El perro es un animalito, pero no es un proyecto, por lo tanto esta opción es {color=#ff0}incorrecta{/color}"
                $renpy.jump(current)
                
            "Resolver los problemas de un país":
                $error="en efecto, eso es incorrecto, el proyecto busca resolver una serie de problemas específicos, hablár de un país es muy general"
                $renpy.jump(current)
            
            "Un sistema con partes que interaccionan entre ellas":
                pass
    label q2:
        show gopher_logo at truecenter
        h "La nube es la opción incorrecta! vamos adelante"
        h "Vamos a ver un ejemplo tangible"
        h "Veamos un reloj..."
        hide gopher_logo
        show reloj at truecenter
        h "El reloj analógico es un {color=#ff0}sistema complejo{/color} que permite saber la hora"
        h "Mediante el movimiento de sus 3 manecillas a diferentes velocidades"
        hide reloj
        show reloj guts at truecenter
        h "para serles sinceros no se como trabajan los relojes, pero lo que sí se"
        h "es que los engranajes (o ruedas dentadas) trabajan de manera coordinada a {color=ff0}diferentes velocidades{/color} para posicionarse"
        h "y contestar a la pregunta {color=#ff0}\"¿Qué hora es?\"{/color}"
        h "Las manecillas se mueven de forma implacable con el pasar de tiempo..."
        h "Vamos a repasar lo aprendido acerca de los relojes en relación a la programación"
        $ error=""
        hide reloj guts
        jump q3
    label q3:
        
        if error !="":
            h "{color=#f00}[error]{/color}"
        menu:
            "¿Cuál de las siguientes afirmaciones es correcta?"
            "El reloj es un sistema simple para resolver una pregunta compleja":
                $error= "¿No es al revés?"
                jump q3
            "Las manecillas del reloj se mueven a la misma velocidad":
                $error = "Así no funcionan los relojes"
                jump q3
            "Los relojes son máquinas complejas que poseen partes sencillas":
                $error= ""
                jump partes1
    label partes1:
        show gopher_logo at truecenter
        h "¡En efecto! aunque el reloj es una máquina aparentemente compleja, que tiene partes sencillas"
        h "Regresando a los proyectos, los proyectos tienen una serie de partes que se relacionan entre sí..."
        h "Pero para serles sinceros no soy un relojero, y conozco muy poco acerca de como funcionan esos aparatos"
        h "Sin embargo, podemos {color=#ff0}imaginar{/color} o deducir de manera correcta que el reloj analógico está compuesto de {color=#ff0}piezas{/color} que trabajan de manera {color=#ff0}coordinada{/color}"
        h "Teniendo en cuenta esto..."
        hide gopher_logo
        $error =""
        jump q4
label q4:
    if error:
        h "{color=#f00}[error]{/color}"
    menu:
        "¿Cuál de estos sistemas complejos, no tiene piezas más simples?"
        "Un carro":
            $ error="No tienes idea lo que cuesta cambiar las {color=ff0}piezas{/color} cuando se daña o lo chocan"
            $ count += 1 
            jump q4
        "El cuerpo humano":
            $error=" Creo que le has quitado el pan a un cirujano...."
            $count += 1
            jump q4
        "Una página web":
            $error="Las páginas web son sistemas muy complejos que interaccionan con el usuarios, tienen una serie de piezas más simples otras páginas, manejan bases de datos, en fin todo un enredo"
            $count += 1
            jump q4
        "Un juego de vídeo":
            $error="Los juegos de video son sistemas muy complejos que interaccionan con el usuarios: tienen piezas más simples que manejan a enemigos, al puntaje, en fin todo un enredo"
            jump q4
        "Clavos":
            h "Eso es correcto!!!"
            jump n2
label n2:
    show gopher_logo at truecenter
    if error == "":
        h "Veo que has acertado a la primera..."
        h "Sin embargo, más adelante verás que cometer errores es muy importante para programar"
    else:
        h "Has seleccionado [count] veces la opción incorrecta"
        h "Cometer errores, es muy importante para aprender cualquier lenguaje de programación..."
    
    h "Existen 2 grandes fases en la programación, la etapa de {color=#ff0}desarrollo{/color} y la etapa de {color=#ff0}producción{/color}"
    h "En la etapa de desarrollo, se DEBEN cometer errores para evitar que éstos vayan a producción"
    h "Además debemos saber que existen 2 tipos de errores: los errores de {color=#ff0}sintaxis{/color} y los errores de {color=#ff0}lógica{/color}"
    h "Los errores de {color=#ff0}sintaxis{/color} impiden al programa traducirse desde el lenguaje de programación el programa, por lo tanto el programa NO CORRE"
    h "Es decir que el programa no corre durante el {color=#ff0}tiempo de ejecución{/color} conocido en inglés como {color=#ff0}runtime{/color}"
    h "Los errores de lógica permiten al programa correr, pero el resultado NO es el esperado"
    h "Un ejemplo de un error de lógica sería un programa que imite a un reloj analógo, el cual CORRE, pero todas las manecillas se mueven a la misma velocidad"
    h "Los errores lógicos son definitivamente muy difíciles de detectar y pueden pasar a la etapa de {color=#ff0}producción{/color} si no somos cuidadosos"
    h "Regresando a la pregunta anterior"
    h "Veo que han notado que a diferencia de objetos o sistemas, los {color=#ff0}clavos{/color} son objectos bastante {color=#ff0}simples{/color}."
    h "Ellos no tienen otras partes dentro y pueden servir para crear objetos más grandes y complejos"
    
    h "El ejercicio de imaginarse como podemos \"desmembrar\" un sistema complejo en sus componentes fundamentales y sus relaciones es el primer paso para poder programar"
    h "A esto se le llama {color=#ff0}abstracción{/color}"
    h "En Python, tenemos algo equivalente a los clavos, pedazos de madera, tornillos o unidades fundamentales"
    h "Los cuales nos van a ayudar a construir sistemas muy complejos"
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    h "La abstracción es tratar de sacar cada una de las piezas que forman un sistema"
    h "Y elaborar un programa con sus partes y las interacción entre esas piezas"
    h "Veamos un ejemplo"
    $count=0
    $error=""
    hide text
    hide gopher_logo
    jump q5
label q5:
    if error != "":
        h "{color=f00}[error]{/}"
    menu:
        "Uno de los siguientes no forman parte del sistema digestivo"
        "El estómago":
            $ error= "estás bromeando?"
            jump q5
        "La tráquea":
            $del error
            jump n3
        "El hígado":
            $error = "El hígado pertenece al aparato digestivo, pero no es parte del \"tubo digestivo\".\nCreo que hay una mejor opción"
            jump q5

label n3:
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    show gopher_logo at truecenter
    h "Qué pregunta más tonta..."
    h "Es cierto que a la tráquea le llega comida de cuando en cuando..."
    h "Pero no en personas sanas..."
    h "Ya que hablamos del sistema digestivo... vamos a hacer algo en relación al mismo"
    python:
        digestivo=["boca","faringe","esófago", "estómago", "intestino delgado", "intestino grueso", "ano"]
        check_organ=""
        counter=9
        
    hide text
    hide gopher_logo
    jump q6
label q6:
    if counter == 9:
        python:
            cabecera= "Señale el órgano del tubo digestivo que se encuentra en la cabeza"
            counter = 0
    else:
        if counter <= 6:
            if check_organ == digestivo[counter]:
                python:
                    counter += 1
                    organo = check_organ
                if counter < 3:
                    $cabecera = "Qué órgano sigue a la "+ organo
                elif counter <7:
                    $cabecera="Qué órgano sigue al " + organo
                else:
                    $cabecera=""
            else:
                if counter > 0 and counter < 6:
                    h "{color=#f00}Ese órgano no es el que sigue!{/color}"
                else:
                    h "{color=#f00}Ese órgano no está en la cabeza!{/color}"
            
    
        
    menu:
        "[cabecera]"
        
        "Ano" if counter < 7:
            $check_organ=digestivo[6]
            jump q6
        "Faringe"if counter < 2:
            $check_organ=digestivo[1]
            jump q6
        "Esófago"if counter < 3:
            $check_organ=digestivo[2]
            jump q6
        "Boca"if counter < 1:
            $check_organ=digestivo[0]
            jump q6
        "Intestino delgado" if counter < 5:
            $check_organ=digestivo[4]
            jump q6
        "Estómago" if counter < 4:
            $check_organ=digestivo[3]
            jump q6
        "Intestino grueso" if counter < 6:
            $check_organ=digestivo[5]
            jump q6
        "Cliq aquí para proseguir" if counter == 7:
            jump n4

label n4:
    show text "{size=40}{color=#000}Capítulo dos\n\n\nLa Abstracción{/color}{/size}" at top
    show gopher_logo at truecenter
    h "Wao, hemos visto como se conectan los órganos del tubo digestivo uno tras otro"
    h "En el caso del carro, del reloj, la página web y del video juego podemos hacer exactamente lo mismo..."
    h "Aún más NO necesitamos ningún programa para ver como estos elementos se relacionan entre sí"
    h "Podemos agarrar un pedazo papel y describir los elementos, su comportamiento, como se relacionan unos con los otros "
    h "Este {color=#ff0}diseño{/color} es fundamental para saber las acciones y definir nuestro programa"
    h "Creo que estamos listos para ver como representamos esos sistemas y elementos en nuestro programa"
    h "Antes de hablar de como hacer esas {color=#ff0}abstracciones{/color} en Python tengo que mostrarles el equivalente a los clavos, engranes y otras piezas fundamentales para crear sistemas complejos"
    h "En Python (como cualquier otro idioma de programación) estos son: las {color=#ff0}variables{/color}, los {color=#ff0}operadores{/color} y las {color=#ff0}funciones{/color}"
    hide text
    show text "{size=40}{color=#000}Capítulo tres\n\n\nPython, la línea de comandos y los scripts (libretos){/color}{/size}" at top
    
    return
