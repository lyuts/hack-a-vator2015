from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.widget import Widget
from widgets.elevatorwidget import ElevatorWidget
from elevator import Elevator, Controller
from person import Person
from floor import Floor
import time


class BuildingCanvas(Widget):
    def setup(self, floors=[], elevators=[]):
        self.__floors = floors
        self.__elevators = elevators

    def update(self, time_delta):
        print "BuildingCanvas::update>", time_delta

	with self.canvas:
	    # Add a red color
	    Color(1., 0, 0)
#            e = ElevatorWidget()
#            e.draw()
            print type(e)

	    # Add a rectangle
#            if not self.r:
#            r = Rectangle(pos=nextPos, size=(500, 500))
#            else:
#                r.pos = nextPos

#	    print type(r.pos[0])
#	    print dir(r.pos)
            

def generateFloors():
    """
    return [ floor1, floor2, ... ]
    """

    NUM_FLOORS = 6
    floors = []
    for id in range(1, NUM_FLOORS + 1):
        floors.append(Floor(id))

    return floors

def generateElevators():
    """
    Generates elevators (or reads them from input)
    return [ elev1, elev2, ... ]
    """

    NUM_ELEVATORS = 6
    elevators = []
    for id in range(1, NUM_ELEVATORS + 1):
        elevators.append(Elevator(id))

    return elevators

class Hackavator(App):
    def build(self):
        floors = generateFloors()
        elevators = generateElevators()

        print "Hackavator with %d floors and %d elevators" % (len(floors), len(elevators))
#        ec = Controller() 

        buildingCanvas = BuildingCanvas()
        buildingCanvas.setup(floors, elevators)

        Clock.schedule_interval(buildingCanvas.update, 1.0)

	return buildingCanvas


if __name__ == '__main__':
    Hackavator().run()

