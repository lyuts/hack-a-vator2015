from singalslot import Signal

class Elevator(object):
    def __init__(self, id, size=10):
        self.__id = id
        self.__people = []
        self.__signal_person_inside = Signal(args=['person'])
        self.__size = size
        self.__velocity = 0

    def stop(self):
        self.__velocity = 0
        # open door
        # close door

    def go_to(floor_no=1):
        # determine current pos
        # change velocity
        # go
        pass

    @property
    def size(self):
        return self.__size

    @property
    def velocity(self):
        return self.__velocity

    @property
    def people(self):
        return self.__people

    @property
    def signal_person_inside(self):
        return self.__signal_person_inside



class Controller(object):
    def __init__(self, num_floors):
        self.__num_floors = num_floors
        self.__elevators = []
        pass

    def elevator_requested(self, from_floor, to_floor):
        pass
