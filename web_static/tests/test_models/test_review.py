#!/usr/bin/python3
"""Libraray for class"""
import unittest
import json
import pep8
import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """implemeneation review"""
    def test_doc_module(self):
        """mode for doc review"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """changes to python 8"""
        python_8 = pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(['models/review.py'])
        self.assertEqual(result_check.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """changes to python 8"""
        python_8 = pep8.StyleGuide(quiet=True)
        result = python_8.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """constructor for the test doc"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """attriubtes for the test class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)

if __name__ == '__main__':
    unittest.main()
