from typing import Callable

from pygame import RESIZABLE, Surface, display, font,  event as pygame_events
from pygame import init as pygame_init, quit as pygame_quit
from pygame.event import Event
from pygame import locals

class Window:
    _instance: Surface
    _event_handlers: dict

    def __init__(self,
        name: str,
        width: int = 500,
        height: int = 300,
        min_width: int = 200,
        min_height: int = 200
    ):
        pygame_init()
        font.init()

        self.min_width = min_width
        self.min_height = min_height
        self._event_handlers = {}

        display.set_caption(name)
        self._instance = display \
            .set_mode((width, height), RESIZABLE) 
            

    def _handle_resize(self, event: Event):
        width = max(self.min_width, event.w)
        height = max(self.min_height, event.h)

        if (width, height) != event.size:
            self._instance = display.set_mode((width, height), RESIZABLE)


    def _handle_event(self, event: Event):
        handler: Callable[[Event], None] | None = self._event_handlers.get(str(event.type), None)
        if(event.type == locals.VIDEORESIZE):
            self._handle_resize(event)

        if(handler is not None):
            handler(event)     


    def event(self, type: int):
        def inner(func: Callable[[Event], None]):
            self._event_handlers[str(type)] = func
            return func
        return inner
    
    def add_event(self, type: int, func: Callable[[Event], None]):
        self._event_handlers[str(type)] = func


    @property
    def smallest_boundary(self):
        width, height = self._instance.get_size()
        return min(width, height)
        
    @property
    def screen_center(self):
        width, height = self._instance.get_size()
        return [width / 2, height / 2]

    @property
    def surface(self):
        return self._instance

    def run(self):
        try:
            while True:
                for event in pygame_events.get():
                    if(event.type == locals.QUIT):
                        pygame_quit()
                        break

                    self._handle_event(event)

                display.flip()
        except KeyboardInterrupt:
            pygame_quit()