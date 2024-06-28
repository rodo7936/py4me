import unittest
from py4me.exceptions import ValidationError
from py4me.serialization import Model



class TestModel(unittest.TestCase):
    def test_model_init_raise_exception(self):
        with self.assertRaises(ValidationError):
            Model(invalid_field='value')

    def test_model_init_readonly_field_raise_exception(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}
            _readonly_fields = {'field'}

        with self.assertRaises(ValidationError):
            DummyModel(field='value')

    def test_model_init_valid(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}

        model = DummyModel(field='value')
        self.assertEqual(model.field, 'value')

    def test_model_repr(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}

        model = DummyModel(field='value')
        self.assertEqual(repr(model), 'DummyModel(field=value)')

    def test_model_eq(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}

        model1 = DummyModel(field='value')
        model2 = DummyModel(field='value')
        self.assertEqual(model1, model2)

    def test_model_serialize_raise_exception(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}

        model = DummyModel(field='value')
        with self.assertRaises(ValidationError):
            model.serialize(invalid_field='value')

    def test_model_serialize_valid(self):
        class DummyModel(Model):
            _fields = {'field': 'value'}

        model = DummyModel(field='value')
        serialized = model.serialize(field='value')
        self.assertEqual(serialized, model)

    def test_model_required_fields(self):
        class DummyModel(Model):
            _fields = {'field': str}
            _required_fields = {'field': str}

        model = DummyModel(field='value')
        self.assertEqual(model.required_fields, {'field': str})

    def test_model_readonly_fields(self):
        class DummyModel(Model):
            _fields = {'field': str}
            _readonly_fields = {'field': str}

        model = DummyModel.serialize(field='value')
        self.assertEqual(model.readonly_fields, {'field': str})

    def test_model_deserialize(self):
        class DummyModel(Model):
            _fields = {'field': str, 'field2': str}
            _readonly_fields = {'field2': str}

        model = DummyModel(field='value')
        self.assertEqual(model.deserialize(), {'field': 'value'})

    def test_model_to_json(self):
        class DummyModel(Model):
            _fields = {'field': str, 'field2': str}
            _readonly_fields = {'field2': str}

        model = DummyModel.serialize(field='value', field2="value2")
        self.assertEqual(model.to_json(), {"field": "value", "field2": "value2"})

    def test_model_deserialize_raise_valid_error(self):
        class DummyModel(Model):
            _fields = {'field': str}
            _required_fields = {'field': str}

        model = DummyModel()
        with self.assertRaises(ValidationError):
            model.deserialize()


if __name__ == '__main__':
    unittest.main()