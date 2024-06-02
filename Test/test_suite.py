# test_suite.py
import unittest
from unit_test import TestViews

suite = unittest.TestLoader().loadTestsFromTestCase(TestViews) 
unittest.TextTestRunner().run(suite)