from window import Window
from pygame import locals

class View:
    def __init__(self, window: Window):
        self.window = window
        self.window.add_event(locals.VIDEORESIZE, lambda _: self.draw())

        self.draw()

    def draw(self):
        print("draw")
