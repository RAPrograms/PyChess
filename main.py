from pygame import locals

from window import Window

window = Window("Chess.py")

@window.event(locals.VIDEORESIZE)
def my_func(event):
    print("Resized", (event.w, event.h))

@window.event(locals.MOUSEBUTTONDOWN)
def my_func(event):
    print("Click", event.pos)


window.run()