from pygame import locals
from window import Window
from view import View

window = Window("Chess.py")

view = View(window)

window.run()