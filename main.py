from model import Model
from window import Window
from view import View

window = Window("Chess.py")

model = Model()
view = View(window=window, model=model)

window.run()