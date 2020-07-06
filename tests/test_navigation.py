import unittest
from jsonnavigator import JsonNavigator


class Test(unittest.TestCase):

    def setUp(self):
        import json
        with open('response.json', 'r') as f:
            self.parsed = json.load(f)
            self.jn = JsonNavigator(self.parsed)

    def test_single_key(self):
        element = self.jn.navigate('ok')
        self.assertEqual(element, True)

    def test_single_key_bogus(self):
        element = self.jn.navigate('nonexistent_key')
        self.assertEqual(element, None)

    def test_index(self):
        element = self.jn.navigate('result', 0)
        self.assertIsInstance(element, dict)

    def test_index_on_dict(self):
        element = self.jn.navigate(0)
        self.assertEqual(element, None)

    def test_mixed_deep_dive(self):
        element = self.jn.navigate('result', 0, 'message', 'from', 'first_name')
        self.assertEqual(element, 'Gilmijar')

    def test_slice(self):
        element = self.jn.navigate('result', slice(2, 3))
        self.assertIsInstance(element, list)
        self.assertEqual(element, self.parsed['result'][2:3])

    def test_slice_on_dict(self):
        element = self.jn.navigate('result', 0, slice(2, 3))
        self.assertEqual(element, None)

    def test_ellipsis_on_list(self):
        element = self.jn.navigate('result', ...)
        self.assertEqual(list(element), self.parsed['result'])

    def test_ellipsis_on_dict(self):
        element = self.jn.navigate('result', 0, ...)
        self.assertEqual(list(element), self.parsed['result'])
        # this fails because subtrees.extend adds dict keys instead of values need to know what to do whhen somehow
