
class Floor(object):
    def __init__(self, num, height=3):
        self.__num = num
        self.__height = height
        self.__people = [] # people currently on the floor (not necessarily waiting for elevators)

    @property
    def height(self):
        return self.__height

    @property
    def num(self):
        return self.__num

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
