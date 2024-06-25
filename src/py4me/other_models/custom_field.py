from typing import Any

from src.py4me.serialization import Model


class CustomField(Model):
    _fields = {
        'id': str,
        'value': Any,
    }

    _required_fields = {
        'id': str,
        'value': Any,
    }