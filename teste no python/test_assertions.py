import unittest


class TestAssertion(unittest.TestCase):

    def test_equals(self):
        #self.assertEquals("one string", "one string")
        self.assertEqual("one string", "other string")
        


if __name__ == '__main__':
    unittest.main()