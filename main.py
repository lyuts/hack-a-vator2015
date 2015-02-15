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

	with self.canvas as canvas:
            canvas_width, canvas_height = self.size

            # clear canvas
            Color(0, 0, 0)
            Rectangle(pos=(canvas_width / 2, 0), size=(canvas_width / 2, canvas_height))

            ELEVATOR_WIDTH_PX = 20
            ELEVATOR_HEIGHT_PX = canvas_height / len(self.__floors)
            FLOOR_WIDTH_PX = canvas_width / 2
            FLOOR_HEIGHT_PX = ELEVATOR_HEIGHT_PX

            # draw floors
            for floor in self.__floors:
                Color(.1 * floor.num, 0, 0)
                x = 0
                y = FLOOR_HEIGHT_PX * (floor.num-1)
                size = (FLOOR_WIDTH_PX, FLOOR_HEIGHT_PX)
                Rectangle(pos=(x, y), size=size)
            
            # draw elevators
            for elevator in self.__elevators:
                Color(0, .1 * elevator.id, 0)
                x = ELEVATOR_WIDTH_PX * (elevator.id - 1)
                y = elevator.position
                size = (ELEVATOR_WIDTH_PX, ELEVATOR_HEIGHT_PX)
                Rectangle(pos=(x, y), size=size)

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

