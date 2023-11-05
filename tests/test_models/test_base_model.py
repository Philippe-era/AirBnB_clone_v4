#!/usr/bin/python3
"""Library of base module tase"""

import json
import pep8
import unittest
import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Basemodel tests running"""

    def test_doc_module(self):
        """Documentation of modules running its course"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Python 8 changes language."""
       python_8= pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Python 8 changes language."""
        python_8 = pep8.StyleGuide(quiet=True)
        result_check = python_8.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result_check.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Documentation constructor"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """Dictionary create"""
        model_create = BaseModel()
        self.assertIs(type(model_create), BaseModel)
        model_create.name = "Holberton"
        model_create.my_number = 89
        self.assertEqual(model_create.name, "Holberton")
        self.assertEqual(model_create.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        model_create_json = model_create.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, model_create_json)
                self.assertIs(type(model_create_json[key]), value)

    def test_base_types(self):
        """base model invented"""
        model_two = BaseModel()
        self.assertIs(type(model_two), BaseModel)
        model_two.name = "Andres"
        model_two.my_number = 80
        self.assertEqual(model_two.name, "Andres")
        self.assertEqual(model_two.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, model_two.__dict__)
                self.assertIs(type(model_two.__dict__[key]), value)

    def test_uuid(self):
        """test for uuid in position"""
        model_check = BaseModel()
        model_check_2 = BaseModel()
        self.assertNotEqual(model_check.id, model_check_2.id)

    def test_datetime_model(self):
        """date time in place"""
        model_check_3 = BaseModel()
        model_check_4 = BaseModel()
        self.assertNotEqual(model_check_3.created_at, model_check_3.updated_at)
        self.assertNotEqual(model_check_3.created_at, model_check_4.created_at)

    def test_string_representation(self):
        """string rep in place"""
        model_create = BaseModel()
        model_create.name = "Holberton"
        model_create.my_number = 89
        model_identity = model_create.id

        info_expected = '[BaseModel] ({}) {}'\
                   .format(model_identity, model_create.__dict__)
        self.assertEqual(str(model_create), info_expected)

    def test_constructor_kwargs(self):
        """constructor in check """
        object_check = BaseModel()
        object_check.name = "Holberton"
        object_check.my_number = 89
        json_attributes = object_check.to_dict()

        object_check2 = BaseModel(**json_attributes)

        self.assertIsInstance(object_check2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(object_check, object_check2)

    def test_file_save(self):
        """files to be saved"""
        batch3 = BaseModel()
        batch3.save()
        with open("file.json", 'r') as f:
            self.assertIn(bacth3.id, f.read())


if __name__ == '__main__':
    unittest.main()

