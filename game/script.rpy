
label start:
    $ musica = ""
    $ current="inicio"
label music_:
    scene white with dissolve
    if musica:
        play music musica
        menu:
            "¿La dejas tocando?"
            "Sí":
                $renpy.jump(current)
            "No, quiero cambiarla":
                stop music
            "No, prefiero estar en silencio":
                stop music
                jump inicio
    menu mus:
        "Seleccione la melodía de fondo, "
        "Poofy Reel":
            $ musica = "Poofy Reel.mp3"
            $renpy.music.set_volume(0.3, delay=0, channel='music')
            jump music_
        "The Show Must Be Go":
            $ musica ="The Show Must Be Go.mp3"
            $ renpy.music.set_volume(0.3, delay=0, channel='music')
            jump music_
        "Ninguno":
            $ musica = "Poofy Reel.mp3"
    
    h ""
    return
