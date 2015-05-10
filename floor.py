from person import Person
from signalslot import Signal

class Floor(object):
    def __init__(self, num, height):
        """
        height = ft
        """
        self.__num = num
        self.__height = height
        self.__people = [] # people currently on the floor (not necessarily waiting for elevators)
        self.__queue = [] # people requested the elevator and currently waiting for one
        self.__signal_elevator_requested = Signal(args=['from_floor', 'to_floor'])
        self.__signal_people_boarded = Signal(args=['elevator_id', 'floor_num', 'people'])

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

    @property
    def signal_people_boarded(self):
        return self.__signal_people_boarded

    def door_opened(self, floor_num, direction, available_capacity, people_inside, elevator_id, **kwargs):

        if floor_num != self.num:
            return

        newcomers = []
        for p in self.queue:
            print 'Checking', p
            if len(people_inside) == 0:
                newcomers.append(p)
            elif len(newcomers) < available_capacity and goes_up == (p.curr_floor < p.dest_floor):
                newcomers.append(p)

        for n in newcomers:
            self.queue.remove(n)

        print 'Floor [%s] %s will board' % (self.num, len(newcomers))
        self.signal_people_boarded.emit(elevator_id=elevator_id, floor_num=self.num, people=newcomers)

    def tick(self, timedelta):
        # example
#        if self.num == 3:
        p = None
        if self.num == 1:
            pass
#            p = Person(self.num, 2)
#            self.people.append(p)
        elif len(self.people) > 0:
            p = self.people.pop(0)

        if p:
            self.signal_elevator_requested.emit(from_floor=p.curr_floor, to_floor=p.dest_floor)
            self.__queue.append(p)

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

    def elevator_doors_open(self, id, **kwargs):
        pass
