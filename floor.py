from person import Person
from signalslot import Signal

class Floor(object):
    def __init__(self, num, height):
        self.__num = num
        self.__height = height
        self.__people = [] # people currently on the floor (not necessarily waiting for elevators)
        self.__queue = [] # people requested the elevator and currently waiting for one
        self.__signal_elevator_requested = Signal(args=['from_floor', 'to_floor'])

    @property
    def height(self):
        return self.__height

    @property
    def num(self):
        return self.__num

    @property
    def people(self):
        return self.__people

    @property
    def queue(self):
        return self.__queue

    @property
    def signal_elevator_requested(self):
        return self.__signal_elevator_requested

    def tick(self, timedelta):
        # example
#        if self.num == 3:
#            p = Person(self.num, 2)
#            self.signal_elevator_requested.emit(from_floor=p.curr_floor, to_floor=p.dest_floor)
        pass
       
    def getNextPerson(self):
        """
        return list of people waiting for the elevator
        """
        # gen random number to represent how many people are waiting
        if self.__num == 1:
            # gen new person
            pass
        else:
            # take new person from the list
            pass

    def elevator_doors_open(self, **kwargs):
        pass
