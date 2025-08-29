from dataclasses.window import Window
from mvc.model import Model
from mvc.view import View

window = Window("Chess.py")

model = Model()
view = View(window=window, model=model)

window.run()