label Go_1:
    h "Vamos a iniciar a aprender Go!"
    $ cuenta=3
label contar:
    if cuenta > 0:
        h "[cuenta]"
        $ cuenta -= 1
        jump contar
    show gopher_logo at truecenter
    h "Listo! iniciamos!"