#!/usr/bin/env python3
"""
    This is a module test from BaseModel class and the methods therein.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime, time
from time import sleep
import models

class TestBaseModel_initialization(unittest.TestCase):
    
    """ Unittests for the initialization of the BaseModel class """
    def test_no_initialization_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_models_unique_ids(self):
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_creation_time(self):
        mod1 = BaseModel()
        sleep(0.05)
        mod2 = BaseModel()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_models_update_time(self):
        mod1 = BaseModel()
        sleep(0.05)
        mod2 = BaseModel()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_args_and_kwargs(self):
        today = datetime.today()
        today_form = today.isoformat()
        mod = BaseModel("12", id="345", created_at=today_form, updated_at=today)
        self.assertEqual(mod.id, "345")
        self.assertEqual(mod.created_at, today)
        self.assertEqual(mod.updated_at, today)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
                BaseModel(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        mod = BaseModel(None)
        self.assertNotIn(None, mod.__dict__.values())

class TestBaseModel_save(unittest.TestCase):                  
        """ Unittests for the save method """
        def test_save1(self):
                mod = BaseModel()
                sleep(0.05)
                updated_at1 = mod.updated_at
                mod.save()
                self.assertLess(updated_at1, mod.updated_at)

        def test_save2(self):
                mod = BaseModel()
                sleep(0.05)
                updated1 = mod.updated_at
                mod.save()
                update2 = mod.updated_at
                self.assertLess(updated1, update2)
                sleep(0.05)
                mod.save()
                self.assertLess(update2, mod.update_at)

class TestBaseModel_to_dict(unittest.TestCase):
        """ unittests for to_dict method """
        def test_dict_type(self):
            mod = BaseModel()
            self.assertTrue(dict, type(mod.to_dict()))

        def test_dict_keys(self):
            base = BaseModel()
            base_dict = base.to_dict()
            self.assertIn('id', base_dict)
            self.assertIn('created_at', base_dict)
            self.assertIn('updated_at', base_dict)
            self.assertIn('__class__', base_dict)

        def test_dict_sample(self):
            base_dict = self.base.to_dict()
            self.assertEqual(dict, type(base_dict))
            self.assertEqual(self.base.id, base_dict["id"])
            self.assertEqual("BaseModel", base_dict["__class__"])
            self.assertEqual(self.base.created_at.isoformat(),
                            base_dict["created_at"])
            self.assertEqual(self.base.updated_at.isoformat(),
                            base_dict["updated_at"])
            self.assertEqual(base_dict.get("_sa_instance_state", None), None)



if __name__ == "__main__":
        unittest.main()
