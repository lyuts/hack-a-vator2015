from signalslot import Signal

class Person(object):
    def __init__(self, curr_floor=0, dest_floor=0):
        self.__curr_floor = curr_floor
        self.__dest_floor = dest_floor
#        self.__request_elevator_signal = Signal(args=['from_floor', 'to_floor'])

    @property
    def curr_floor(self):
        return self.__curr_floor

    @property
    def dest_floor(self):
        return self.__dest_floor

#    @property
#    def request_elevator(self):
#        return self.__request_elevator_signal
