from kivy.app import App
from kivy.graphics import *
from kivy.uix.widget import Widget
from widgets.elevatorwidget import ElevatorWidget
import elevator
from person import Person
import time


class BuildingCanvas(Widget):
#    def __init__(self):
#        self.r = None

    def update(self, dt):
        pass

    def d(self, nextPos=(10, 10)):
	with self.canvas:
	    # Add a red color
	    Color(1., 0, 0)
            e = ElevatorWidget()
#            e.draw()
            print type(e)

	    # Add a rectangle
#            if not self.r:
#            r = Rectangle(pos=nextPos, size=(500, 500))
#            else:
#                r.pos = nextPos

#	    print type(r.pos[0])
#	    print dir(r.pos)
            

class Hackavator(App):
    def build(self):
        Clock.schedule_interval(BuildingCanvas.update, 1.0)
        ec = ElevatorController() 
	#print dir(BuildingCanvas())

        floors = generateFloors()
        elevators = generateElevators()

        buildingCanvas = BuildingCanvas()
        buildingCanvas.setFloors(floors)
        buildingCanvas.setElevators(elevators)

	return buildingCanvas


if __name__ == '__main__':
    Hackavator().run()

