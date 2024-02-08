#!/usr/bin/env python3
""" Module for testing BaseModel from models module """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Class for testing BaseModel """

    def setUp(self):
        """ Set up test instance """

        self.model = BaseModel()

    def test_init(self):
        """ Test initialization """

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """ Test __str__ method """

        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """ Test save method """

        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """ Test to_dict method """

        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(
            model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(
            model_dict["updated_at"], self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
