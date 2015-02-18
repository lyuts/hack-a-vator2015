from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.widget import Widget
from widgets.elevatorwidget import ElevatorWidget
from elevator import Elevator, Controller
from person import Person
from floor import Floor
import time
from kivy.uix.label import Label

FLOOR_HEIGHT_PX = 50
ELEVATOR_HEIGHT_PX = FLOOR_HEIGHT_PX
UPDATE_INTERVAL_SEC = 1.0

class BuildingCanvas(Widget):

    def setup(self, floors=[], elevators=[]):
        self.__floors = floors
        self.__elevators = elevators

    def update(self, time_delta):
        print "BuildingCanvas::update>", time_delta
        self.canvas.clear()
	with self.canvas as canvas:
            canvas_width, canvas_height = self.size

            # clear canvas
            Color(0, 0, 0)
            Rectangle(pos=(canvas_width / 2, 0), size=(canvas_width / 2, canvas_height))

            ELEVATOR_WIDTH_PX = 20
#            ELEVATOR_HEIGHT_PX = canvas_height / len(self.__floors)
            FLOOR_WIDTH_PX = canvas_width / 2
#            FLOOR_HEIGHT_PX = ELEVATOR_HEIGHT_PX

            # draw floors
            y = 0
            for floor in self.__floors:
                Color(.1 * floor.num, 0, 0)
                x = 0
                size = (FLOOR_WIDTH_PX, FLOOR_HEIGHT_PX)
                Rectangle(pos=(x, y), size=size)
                Color(1., 1., 1.)
                l = Label(text=str('%s/%s' % (len(floor.queue), len(floor.people))), pos=(x + FLOOR_WIDTH_PX / 2, y + FLOOR_HEIGHT_PX / 2))
                l.size = l.texture_size
#                l.texture_update()
                y += floor.height

            # draw elevators
            for elevator in self.__elevators:
                Color(0, .1 * elevator.id, 0)
                x = ELEVATOR_WIDTH_PX * (elevator.id - 1)
                y = elevator.position
                size = (ELEVATOR_WIDTH_PX, ELEVATOR_HEIGHT_PX)
                Rectangle(pos=(x, y), size=size)
                Color(1., 1., 1.)
                l = Label(text=str(len(elevator.people)), pos=(x + ELEVATOR_WIDTH_PX / 2, y + ELEVATOR_HEIGHT_PX / 2))
                l.size =  l.texture_size

def generateFloors():
    """
    return [ floor1, floor2, ... ]
    """

    NUM_FLOORS = 6
    floors = []
    for num in range(1, NUM_FLOORS + 1):
        floor = Floor(num=num, height=FLOOR_HEIGHT_PX)
        floors.append(floor)
        Clock.schedule_interval(floor.tick, UPDATE_INTERVAL_SEC)

    return floors

def generateElevators():
    """
    Generates elevators (or reads them from input)
    return [ elev1, elev2, ... ]
    """

    NUM_ELEVATORS = 6
    elevators = []
    for id in range(1, NUM_ELEVATORS + 1):
        elevator = Elevator(id)
        elevators.append(elevator)

        Clock.schedule_interval(elevator.move, UPDATE_INTERVAL_SEC)

    return elevators

def setupSignalSlots(controller, floors, elevators):
    for floor in floors:
        floor.signal_elevator_requested.connect(controller.elevator_requested)

    for elevator in elevators:
        elevator.signal_position_change.connect(controller.elevator_position_changed)

        controller.signal_change_velocity.connect(elevator.set_velocity)
        controller.signal_stop.connect(elevator.stop)


class Hackavator(App):
    def build(self):

        floors = generateFloors()
        elevators = generateElevators()

        ec = Controller(floors, elevators) 

        setupSignalSlots(ec, floors, elevators)

        print "Hackavator with %d floors and %d elevators" % (len(floors), len(elevators))

        buildingCanvas = BuildingCanvas()
        buildingCanvas.setup(floors, elevators)

        Clock.schedule_interval(buildingCanvas.update, UPDATE_INTERVAL_SEC)

	return buildingCanvas


if __name__ == '__main__':
    Hackavator().run()

