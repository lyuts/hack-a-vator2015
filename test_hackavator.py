from mock import Mock, patch
from person import Person
from floor import Floor
from elevator import Elevator, Controller
from signalslot import Signal
import unittest

@patch('signalslot.signal.inspect')
class FloorUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self, method):
        f = Floor(num=1, height=10)
        self.assertEqual(1, f.num)
        self.assertEqual(10, f.height)
        self.assertTrue(type(f.signal_elevator_requested) is Signal)
        self.assertTrue(type(f.people) is list)
        self.assertTrue(type(f.queue) is list)

    def test_request_elevator(self, method):
        observer = Mock()

        f = Floor(num=0, height=0)
        f.signal_elevator_requested.connect(observer)
        f.signal_elevator_requested.emit(from_floor=1, to_floor=2)

        observer.assert_called_once_with(from_floor=1, to_floor=2)

class ElevatorUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_properties(self):
        e = Elevator(id=6, size=7, height=17)
        self.assertEqual(6, e.id)
        self.assertEqual(7, e.size)
        self.assertEqual(17, e.height)
        self.assertTrue(type(e.signal_person_inside) is Signal)
        self.assertTrue(type(e.signal_position_change) is Signal)
        self.assertTrue(type(e.velocity) is int)
        self.assertTrue(type(e.position) is int)
        self.assertTrue(type(e.people) is list)

    def test_poisition_change(self):
        e = Elevator(id=6, size=7)

        observer = Mock()

        f = Floor(num=0, height=0)
        e.signal_position_change.connect(observer)
        e.signal_elevator_requested.emit(from_floor=1, to_floor=2)

        observer.assert_called_once_with(from_floor=1, to_floor=2)

class PersonUnitTests(unittest.TestCase):
    def test_properties(self):
        p = Person(curr_floor=2, dest_floor=1)
        self.assertEqual(2, p.curr_floor)
        self.assertEqual(1, p.dest_floor)

class ControllerUnitTests(unittest.TestCase):
    def test_default_contruction(self):
        c = Controller()

    def test_properties(self):
        floors = [ Floor(1, 7), Floor(2, 7) ]
        elevators = [ Elevator(id=1, size=10)]

        c = Controller(floors, elevators)

        self.assertTrue(type(c.signal_change_velocity) is Signal)
        self.assertTrue(type(c.signal_stop) is Signal)

if __name__ == "__main__":
    unittest.main()
