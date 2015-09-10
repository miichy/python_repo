#!/usr/bin/python

# unittest

import unittest

class TestS(unittest.TestCase):
    def testt(self):
        self.assertEqual(1+1,2)

    def testm(self):
        self.assertTrue(1)

if __name__ == '__main__':
    unittest.main()
