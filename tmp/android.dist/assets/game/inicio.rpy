init python:
    import re
    import os
    tipJar="https://www.paypal.me/HedleyQuintana"
    enlaces=False
    now_playing="Poofy Reel"
    musica="Poofy Reel.mp3"
    info=False
    subtitle = Position(xpos=0.5, xanchor='center', ypos=0.60,
                   yanchor='top')
    def cambiarMusica(m):
        global musica, now_playing
        lm=['The Show Must Be Go.mp3','Poofy Reel.mp3']
        if not m:
            m=lm[1]
        lm.remove(m)
        musica = lm[0]
        now_playing=musica[:-4]
        renpy.play(musica, 'music')
   
    
image gopher_logo =Image("images/gopher.jpg",xalign=0.5, yalign=0.5)
image renpy_logo =Image("images/renpy logo.png", xalign=0.5, yalign=0.2)
image reloj=im.FactorScale("images/reloj.png", 0.25)
image reloj guts=im.FactorScale("images/reloj engranajes.jpg", 0.25)
image pitagoras=Image('images/pitagoras.png')
image canvas=Image('images/Canvas.png')
image white ="#ffffff"
define h = Character('Hedley', color="#c8ffc8")
define consola = Character('Consola de Python', color="#00cc00")