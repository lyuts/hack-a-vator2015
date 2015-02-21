from elevator import Elevator, Controller
from floor import Floor
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from person import Person
from widgets.elevatorwidget import ElevatorWidget
import itertools
import time

FLOOR_HEIGHT_PX = 50
ELEVATOR_HEIGHT_PX = FLOOR_HEIGHT_PX
UPDATE_INTERVAL_SEC = .1

class BuildingCanvas(Widget):

    def setup(self, floors=[], elevators=[]):
        self.__floors = floors
        self.__elevators = elevators

        self.__floorWidgets = {}
        self.__floorLabels = {}
        self.__elevatorWidgets = {}
        self.__elevatorLabels = {}

        with self.canvas:
            for floor in self.__floors:
                Color(.1 * floor.num, 0, 0)
                self.__floorWidgets[floor] = Rectangle()
                Color(1., 1., 1.)
                self.__floorLabels[floor] = Label()

            for elevator in self.__elevators:
                Color(0, .1 * elevator.id, 0)
                self.__elevatorWidgets[elevator] = Rectangle()
                Color(1., 1., 1.)
                self.__elevatorLabels[elevator] = Label()


    def update(self, time_delta):
#        print "BuildingCanvas::update>", time_delta
	with self.canvas as canvas:
            canvas_width, canvas_height = self.size

            ELEVATOR_WIDTH_PX = 20
#            ELEVATOR_HEIGHT_PX = canvas_height / len(self.__floors)
            FLOOR_WIDTH_PX = canvas_width / 2
#            FLOOR_HEIGHT_PX = ELEVATOR_HEIGHT_PX

            # draw floors
            y = 0
            for floor in self.__floors:
                rect = self.__floorWidgets[floor]
                lbl = self.__floorLabels[floor]

                x = 0

                rect.size = (FLOOR_WIDTH_PX, floor.height)
                rect.pos = (x, y)

#                print 'Before', lbl.text, lbl.pos, lbl.size, lbl.texture_size
                lbl.text = '%s/%s' % (len(floor.queue), len(floor.people))
                lbl.size = lbl.texture_size
                lbl.pos = (x + FLOOR_WIDTH_PX / 2, y + floor.height / 2)
#                print 'After', lbl.text, lbl.pos, lbl.size, lbl.texture_size
                lbl.texture_update()
                y += floor.height

            # draw elevators
            for elevator in self.__elevators:
                rect = self.__elevatorWidgets[elevator]
                lbl = self.__elevatorLabels[elevator]

                x = ELEVATOR_WIDTH_PX * (elevator.id - 1)
                y = elevator.position

                rect.pos = (x, y)
                rect.size = (ELEVATOR_WIDTH_PX, elevator.height)

                lbl.text = str(len(elevator.people))
                lbl.size =  lbl.texture_size
                lbl.pos = (x + ELEVATOR_WIDTH_PX / 2, y + elevator.height / 2)
                lbl.texture_update()


def generateFloors():
    """
    return [ floor1, floor2, ... ]
    """

    NUM_FLOORS = 3
    floors = []
    for num in range(1, NUM_FLOORS + 1):
        floor = Floor(num=num, height=FLOOR_HEIGHT_PX)
        floors.append(floor)
        Clock.schedule_interval(floor.tick, UPDATE_INTERVAL_SEC)

    # remove this
    floors[-1].people.append(Person(floors[-1].num, 1))


    return floors

def generateElevators():
    """
    Generates elevators (or reads them from input)
    return [ elev1, elev2, ... ]
    """

    NUM_ELEVATORS = 6
    elevators = []
    for id in range(1, NUM_ELEVATORS + 1):
        elevator = Elevator(id, height=ELEVATOR_HEIGHT_PX)
        elevators.append(elevator)

        Clock.schedule_interval(elevator.move, UPDATE_INTERVAL_SEC)

    return elevators

def setupSignalSlots(controller, floors, elevators):
    for floor in floors:
        floor.signal_elevator_requested.connect(controller.elevator_requested)

    for elevator in elevators:
        elevator.signal_position_change.connect(controller.elevator_position_changed)
        elevator.signal_door_closed.connect(controller.elevator_door_closed)

        controller.signal_change_velocity.connect(elevator.set_velocity)
        controller.signal_stop.connect(elevator.stop)

    for e, f in itertools.product(elevators, floors):
        e.signal_door_opened.connect(f.door_opened)
        f.signal_people_boarded.connect(e.people_boarded)


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

