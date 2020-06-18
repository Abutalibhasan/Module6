import unittest
from more_functions import string_fuctions


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        res = string_fuctions.multiply_string("Abutalib", 3)
        self.assertEqual(res, "AbutalibAbutalibAbutalib")


if __name__ == '__main__':
    unittest.main()
