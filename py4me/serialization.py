from py4me.exceptions import ValidationError


class Model(object):
    _required_fields = {}
    _fields = {}
    _readonly_fields = {}
    _validation = {}

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self._fields:
                raise ValidationError(f"Key {k} is not supported in model: {self.__class__.__name__}")
            if k in self._readonly_fields:
                raise ValidationError(f"Key {k} is readonly in model: {self.__class__.__name__}")
            setattr(self, k, v)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({', '.join([f'{k}={getattr(self, k)}' for k in self.__dict__ if k in self.fields])})")

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False
        return all([getattr(self, k) == getattr(other, k) for k in self.fields])

    @property
    def required_fields(self):
        return self._required_fields

    @property
    def fields(self):
        return self._fields

    @classmethod
    @property
    def model_fields(cls):
        return cls._fields

    @property
    def readonly_fields(self):
        return self._readonly_fields

    def _serialize(self, **data):
        for k, v in data.items():
            if k not in self._fields:
                raise ValidationError(f"Key {k} is not supported in model: {self.__class__.__name__}")
            setattr(self, k, v.serialize() if isinstance(v, Model) else v)
        return self

    @classmethod
    def serialize(cls, **data) -> 'Model':
        return cls()._serialize(**data)

    def deserialize(self):
        return DeSerializer.to_post_patch_method(self)

    def to_json(self):
        return DeSerializer.to_json(self)


class DeSerializer:

    @classmethod
    def to_post_patch_method(cls, model: Model) -> dict:
        reqs = model.required_fields
        if not all([getattr(model, k, None) for k in reqs]):
            raise ValidationError("All required field must be set!")
        return {k: getattr(model, k).deserialize() if isinstance(getattr(model, k), Model) else getattr(model, k) for k
                in model.fields if k not in model.readonly_fields and getattr(model, k, None) is not None}

    @classmethod
    def to_json(cls, model: Model) -> dict:
        return {k: getattr(model, k).to_json() if isinstance(getattr(model, k), Model) else getattr(model, k) for k in
                model.fields if getattr(model, k, None) is not None}
