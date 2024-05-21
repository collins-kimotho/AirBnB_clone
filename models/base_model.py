#!/usr/bin/python3
"""
Base class for all other classes in the AirBnB clone project.

Attributes:
    id (str): Unique identifier for the instance.
    created_at (datetime): Creation timestamp.
    updated_at (datetime): Last update timestamp.
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute names and values.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all keys/values of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String in the format.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

# Example usage:


if __name__ == "__main__":
    base_model = BaseModel()
    print(base_model)
    base_model.save()
    print(base_model.to_dict())
