#!/usr/bin/env python3
""" Module for testing FileStorage from models.engine module """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test cases for the FileStorage class """

    def setUp(self):
        """ Setup for all tests """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.name = "Test"
        self.model.my_number = 42

    def tearDown(self):
        """ Teardown for all tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """ Test the all method """
        self.storage.new(self.model)
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """ Test the new method """
        self.storage.new(self.model)
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

    def test_save(self):
        """ Test the save method """
        self.storage.new(self.model)
        self.storage.save()
        with open("file.json", "r") as f:
            objs = json.load(f)
        self.assertIn("BaseModel." + self.model.id, objs)

    def test_reload(self):
        """ Test the reload method """
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.model.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
