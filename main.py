from classes.window import Window
from mvc.controller import Controller
from mvc.model import Model
from mvc.view import View

window = Window("Chess.py")

view = View(window=window)
model = Model()

controller = Controller(model=model, view=view)

window.run()