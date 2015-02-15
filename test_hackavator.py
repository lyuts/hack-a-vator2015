from mock import Mock
from person import Person
import unittest

class PersonUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_request_elevator(self):
        p = Person(0, 0)
        observer = Mock()
        invoked_floor_pair = { 'count' : 0}

        def custom_slot(**kwargs):
            invoked_floor_pair['from_floor'] = kwargs['from_floor']
            invoked_floor_pair['to_floor'] = kwargs['to_floor']
            invoked_floor_pair['count'] += 1

        p.request_elevator.connect(custom_slot)
        p.request_elevator.emit(from_floor=1, to_floor=2)

        self.assertEqual(1, invoked_floor_pair['from_floor'])
        self.assertEqual(2, invoked_floor_pair['to_floor'])
        self.assertEqual(1, invoked_floor_pair['count'], 'There should be exactly 1 invocation')

if __name__ == "__main__":
    unittest.main()
