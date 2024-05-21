#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all AirBnB clone models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'created_at' in kwargs and isinstance(kwargs
                                                     ['created_at'], str):
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs and isinstance(kwargs
                                                     ['updated_at'], str):
                self.updated_at = datetime.fromisoformat(
                    kwargs['updated_at']
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Returns a string representation of the instance."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
