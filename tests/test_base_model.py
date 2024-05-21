# tests/test_base_model.py
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_attributes(self):
        """Test initialization of BaseModel attributes."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_generation(self):
        """Test if the ID is generated properly."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test the save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        """Test initialization of BaseModel with kwargs."""
        now = datetime.now().isoformat()
        model_data = {
            'id': 'test_id',
            'created_at': now,
            'updated_at': now,
            'name': 'test_name'
        }
        model = BaseModel(**model_data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at.isoformat(), now)
        self.assertEqual(model.updated_at.isoformat(), now)
        self.assertEqual(model.name, 'test_name')

if __name__ == '__main__':
    unittest.main()
