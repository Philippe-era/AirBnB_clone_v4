#!/usr/bin/python3
"""Library for state class"""
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Implemenetation of Test STATE"""
    def test_doc_module(self):
        """Module documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """Test that models/state.py will/or conforms to PEP8."""
        python_8 = pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(['models/state.py'])
        self.assertEqual(result_check.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """changes language to python 8"""
        python_8 = pep8.StyleGuide(quiet=True)
        result = python_8.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor of the doc class"""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Class is for killers you check"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)

if __name__ == '__main__':
    unittest.main()
