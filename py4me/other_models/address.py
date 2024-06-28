from py4me.serialization import Model


class Address(Model):
    _fields = {
        'address': str,
        'city': str,
        'zip" str,'
        'country': str,
        'id': int,
        'integration': bool,
        'label': 'AddressLabel',
        'state': str,
    }

    _readonly_fields = {
        'id': int,
    }
