from dataclasses.window import Window
from mvc.controller import Controller
from mvc.model import Model
from mvc.view import View

window = Window("Chess.py")

model = Model()
view = View(window=window, model=model)

controller = Controller(model=model, view=view)

window.run()