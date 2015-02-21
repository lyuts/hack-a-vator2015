from signalslot import Signal
from kivy.vector import Vector
import time

class Elevator(object):
    def __init__(self, id, size=10, height=10):
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
        # direction: True = up, Down = False
        self.__signal_door_opened = Signal(args=['id', 'direction', 'people_inside', 'available_capacity', 'floor_num'])
        self.__signal_door_closed = Signal(args=['id', 'people_inside'])
        self.__size = size
        self.__velocity = 0
        self.__position = (0, 0)
        self.__height = height
        self.__door_opening_time = 1.5
        self.__door_closing_time = 2.5

    def move(self, timedelta):
#        print '[%s] speed = %s/%s' % (self.id, self.velocity, self.__velocity)
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
        kwargs['floor_num']
        """
        if self.id != kwargs['id']:
            return

        floor_num = kwargs['floor_num']
        going_up = self.__velocity > 0

        self.__velocity = 0
        # open door
#        time.sleep(self.__door_opening_time)

        self.signal_door_opened.emit(id=self.id, direction=going_up, available_capacity=self.size - len(self.people), people_inside=self.people[:], floor_num=floor_num)


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

    @property
    def height(self):
        return self.__height

    @property
    def signal_door_opened(self):
        print 'signaling door opened', self.id
        return self.__signal_door_opened

    @property
    def signal_door_closed(self):
        return self.__signal_door_closed

    def people_boarded(self, **kwargs):
        if self.id != kwargs['elevator_id']:
            return

        newcomers = kwargs['people']
        self.people.extend(newcomers)

        # close door
#        time.sleep(self.__door_closing_time)

        self.signal_door_closed.emit(id=self.id, people_inside=self.people[:])

class Controller(object):
    def __init__(self, floors=[], elevators=[]):
        self.__floors = floors

        # absolute coords
        self.__floor_coords = [0] * len(self.__floors)
        for i in range(1, len(self.__floor_coords)):
            self.__floor_coords[i] += self.__floor_coords[i-1] + self.__floors[i-1].height

        self.__elevators = {e.id : e for e in elevators}
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
        for e in self.__elevators.values():
            if e.velocity == 0:
                self.signal_change_velocity.emit(id=e.id, velocity=2)
        pass

    def elevator_position_changed(self, **kwargs):
        """
        kwargs['id']
        kwargs['x']
        kwargs['y']
        """
        id = kwargs['id']
        y = kwargs['y']

        FORCED_STOP_DIST = .33 # 10cm range for allowed stop
        # if about to hit ground/roof -> stop
        if abs(y - self.__floor_coords[-1]) < FORCED_STOP_DIST and self.__elevators[id].velocity > 0:
            self.__signal_stop.emit(id=id, floor_num=len(self.__floors))
        elif abs(y - self.__floor_coords[0]) < FORCED_STOP_DIST and self.__elevators[id].velocity < 0:
            self.__signal_stop.emit(id=id, floor_num=1)
        else:
            pass
            # if near the destination floor -> stop

#        assert y <= self.__floor_coords[-1], 'elevator hit the roof'

#        print y, self.__floor_coords
        # calculate position, and if at floor, and floor is in dest list, then signal stop
        pass

    def elevator_door_closed(self, **kwargs):
        pass
