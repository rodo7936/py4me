import logging

from src.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class Model:
    _attributes = {}  # dict of attributes with their types

    _read_only = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self._attributes:
                _logger.warning(f'Unknown attribute {key} for {self.__class__.__name__}')
            elif key in self._read_only:
                _logger.warning(f'Attribute {key} is read only for {self.__class__.__name__}, skipping')
            else:
                setattr(self, key, value)

    def validate(self):
        for key, value in self.__dict__.items():
            if key in self._attributes:
                if not isinstance(value, self._attributes[key]):
                    raise ValidationError(f'Attribute {key} is not of type {self._attributes[key]}')

    def _serialize(self):
        ...


    def _deserialize(self):
        ...


class Serializer:
    client_side_validation = False
    # For future usage maybe

    def __init__(self, obj: Model):
        self._obj = Model

    def serialize(self, keep_readonly: bool = False):
        retr = {}
        if self.client_side_validation:
            self._obj.validate()
        for key, value in self._obj.__dict__.items():
            if key in self._obj._attributes:
                if key in self._obj._read_only:
                    if keep_readonly:
                        retr[key] = value._serialize() if isinstance(value, Model) else value
                    else:
                        _logger.warning(f'Attribute {key} is read only for {self._obj.__class__.__name__}, skipping')
                else:
                    retr[key] = value
        return retr
