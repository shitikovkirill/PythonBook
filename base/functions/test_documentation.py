from __future__ import absolute_import
import unittest

class TestFunctionMethods(unittest.TestCase):
    def test_docs(self):
        def my_function():
            """Do nothing, but document it.
            No, really, it doesn't do anything."""
            pass

        self.assertEqual('Do nothing, but document it.\n            No, really, it doesn\'t do anything.', my_function.__doc__)