label linea_de_comandos_1:
    h "Vamos a iniciar hablando de la \"linea de comandos\" o \"terminal\""
    h "El uso de la linea de comandos es fundamental para el manejo del lenguaje Go"
    h "En el caso del lenguaje Go, este es un lenguaje {color=#ff0}compilado{/color},\nes decir que una vez que escribimos los archivos que forman el programa o script en Go, debemos traducirlo a un programa ejecutable, es decir {color=#ff0}compilarlo{/color}"
    h "El lenguaje Go hace un programa el cual se puede ejecutar o compilar"
    if renpy.windows:
        h "Dado que esta es una computadora Windows, podremos abrir la \"linea de comandos\" desde el boton de inicio de Windows"
        h "Para correr este programa, escribimos cmd.exe y vemos la ventana negra del mal de {color=#ff0}linea de comandos{/color}"
        h "Dado que vamos a trabajar en Go o Golang requerimos tener siempre a la mano un atajo para este programa"
        h "Debemos correr esta con privilegios de administrador o privilegios elevados para hacer otras operaciones pertinentes"
        $ cmd="línea de comandos"
    elif renpy.mac:
        h "Dado que esta es una computadora Mac OS, podremos abrir la \"terminal\" buscandola en el Finder"
        h "Dado que vamos a trabajar en Go o Golang requerimos tener siempre a la mano un atajo para este programa"
        h "Es una muy buena idea un atajo de la terminal en el Docker del escritorio"
        $ cmd="terminal"
    elif renpy.mobile:
        h "Este es un dispositivo movil, por lo tanto no se puede correr o complar nada en el lenguaje Go en este mommento"
        $ cmd="línea de comandos para Windows o terminal para sistemas operativos parecidos a Unix"
    else: 
        h "Dado que esta es una computadora linux, podremos abrir la \"terminal\" como es usual en este sistema operativo"
        h "Existen 3 terminales en Linux: terminal de gnome, la terminal de xterm (y su primito UXTerm) y la interfase de terminal"
        h "La terminal es parte integral del manejo de linux, y en los escritorios es fácil de buscar"
        h "en el caso de U"
        $ cmd= "terminal"
    h "Una vez que sabemos como acceder a la [cmd], podemos proseguir a instalar Go"
    h "Vamos a instalar Go "
    if renpy.mobile:
        h "Debido a que este es un dispositivo mobil te recomiendo que intentes utilizar una computadora de escritorio con permisos de usuario raiz o administrador para instalar este programa"
        h "De este modo sacaras mucho mejor provecho de este curso"
        h "De todos modos te deja qui te dejo las instrucciones de como instalar el programa"
    h "Es cosa de bajar el instalador y seguir las instrucciones de la {a=https://golang.org/dl} la página de descargas{/a}"
    h "Antes de dar un paso más, voy a hablarles de las {color=#ff0}variables de entorno{/color}"
    h "Voy a describirles el concepto de {color=#ff0}variables de entorno{/color}"
    h "Para entender el concepto de las {color=#ff0}variables de entorno{/color} primero debemos entender como funcionan los íconos"
    h "El comportamiento de los íconos es el mismo independiente"
    return
    
    