from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

class ElevatorWidget(Widget):
    def __init__(self):
        self.velocity_x = NumericProperty(0)
        self.velocity_y = NumericProperty(0)
        self.velocity = ReferenceListProperty(self.velocity_x, self.velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
