from signalslot import Signal
from kivy.vector import Vector

class Elevator(object):
    def __init__(self, id, size=10):
        """
        people - list of people currently in the elevator
        size - elevator capacity in terms of people count
        velocity - velocity along y axis
        position - current y coordinate
        """
        self.__id = id
        self.__people = []
        self.__signal_person_inside = Signal(args=['person'])
        self.__signal_position_change = Signal(args=['id', 'x', 'y'])
        self.__size = size
        self.__velocity = 0
        self.__position = (0, 0)

    def move(self, timedelta):
        self.__position = Vector(0, self.__velocity) + self.__position
        self.__signal_position_change.emit(id=self.__id, x=self.__position[0], y=self.__position[1])

    def set_velocity(self, **kwargs):
        """
        kwargs['id']
        kwargs['velocity']
        """
        if self.id == kwargs['id']:
            self.__velocity = kwargs['velocity']

    def stop(self, **kwargs):
        """
        kwargs['id']
        """
        if self.id != kwargs['id']:
            return

        self.__velocity = 0
        # open door
        # close door

    def go_to(floor_no=1):
        # determine current pos
        # change velocity
        # go
        pass

    @property
    def id(self):
        return self.__id

    @property
    def size(self):
        return self.__size

    @property
    def velocity(self):
        return self.__velocity

    @property
    def position(self):
        """
        Simplified for elevator case, as it moves up/down
        Return y coordinate
        """
        return self.__position[1]

    @property
    def people(self):
        return self.__people

    @property
    def signal_person_inside(self):
        return self.__signal_person_inside

    @property
    def signal_position_change(self):
        return self.__signal_position_change



class Controller(object):
    def __init__(self, floors=[], elevators=[]):
        self.__floors = floors

        # relative coords
        self.__floor_coords = map(lambda x: x.height, self.__floors)
        # absolute coords
        for i in range(1, len(self.__floor_coords)):
            self.__floor_coords[i] += self.__floor_coords[i-1]

        self.__elevators = elevators
        # indicates a command to an elevator to change velocity
        self.__signal_change_velocity = Signal(args=['id', 'velocity'])
        self.__signal_stop = Signal(args=['id'])

    @property
    def signal_change_velocity(self):
        return self.__signal_change_velocity

    @property
    def signal_stop(self):
        return self.__signal_stop

    def elevator_requested(self, **kwargs):
        """
        kwargs['from_floor']
        kwargs['to_floor']
        """
        print "Controller::elevator_requested>", kwargs
        for e in self.__elevators:
            if e.velocity == 0:
                self.signal_change_velocity.emit(id=e.id, velocity=2)
        pass

    def elevator_position_changed(self, **kwargs):
        """
        kwargs['id']
        kwargs['x']
        kwargs['y']
        """
        # calculate position, and if at floor, and floor is in dest list, then signal stop
        pass
