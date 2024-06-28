from py4me.serialization import Model


class Organization(Model):
    _fields = {
        'id': int,
        'name': str,
    }
    _required_fields = {
        'name': str
    }

    _readonly_fields = {
        'id': int
        }

    _validation = {

        }
