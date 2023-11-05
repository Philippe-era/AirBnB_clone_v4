#!/usr/bin/python3
"""Library test city"""
import unittest
import datetime
import json
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """implementation of city"""
    def test_doc_module(self):
        """module creation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """changes to python 8."""
        python_8 = pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(['models/city.py'])
        self.assertEqual(result_check.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """changes to python 8"""
        python_8 = pep8.StyleGuide(quiet=True)
        res = python_8.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """documentation of constructor in place"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """class check in place you feel me"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()

