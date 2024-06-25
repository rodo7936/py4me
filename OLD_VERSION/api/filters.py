from typing import Any


class Filter:
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value


class GreaterThanFilter(Filter):
    """
    Filter for checking if field is greater than value
    """
    def __str__(self):
        return f'{self.field}>{self.value}'


class LessThanFilter(Filter):
    """
    Filter for checking if field is less than value
    """
    def __str__(self):
        return f'{self.field}<{self.value}'


class EqualFilter(Filter):
    """
    Filter for checking if field is equal to value
    """
    def __str__(self):
        return f'{self.field}={self.value}'


class NotEqualFilter(Filter):
    """
    Filter for checking if field is not equal to value
    """
    def __str__(self):
        return f'{self.field}!={self.value}'


class GreaterOrEqualFilter(Filter):
    """
    Filter for checking if field is greater or equal to value
    """
    def __str__(self):
        return f'{self.field}=>{self.value}'


class LessOrEqualFilter(Filter):
    """
    Filter for checking if field is less or equal to value
    """
    def __str__(self):
        return f'{self.field}=<{self.value}'


class PresentFilter(Filter):
    """
    Filter for checking if field is present and contains value
    """
    def __str__(self):
        return f'{self.field}=!'


class EmptyFilter(Filter):
    """
    Filter for checking if field is empty
    """
    def __str__(self):
        return f'{self.field}='


class NotInFilter(Filter):
    """
    Filter for checking if field is not in list of values
    """
    def __str__(self):
        if self.value.__iter__:
            return f'{self.field}=!{",".join(self.value)}'
        if isinstance(self.value, str):
            return f'{self.field}=!{self.value}'
        return f'{self.field}=!{self.value}'


class InFilter(Filter):
    """
    Filter for checking if field is in list of values
    """
    def __str__(self):
        if self.value.__iter__:
            return f'{self.field}={",".join(self.value)}'
        if isinstance(self.value, str):
            return f'{self.field}={self.value}'
        return f'{self.field}={self.value}'


class GreaterThanLessThanFilter(Filter):
    """
    Filter for checking if field is greater than value and less than value
    """
    def __str__(self):
        return f'{self.field}>{self.value[0]}<{self.value[1]}'


class GreaterThanEqualLessThanEqualFilter(Filter):
    """
    Filter for checking if field is greater or equal to value and less or equal to value
    """
    def __str__(self):
        return f'{self.field}>={self.value[0]}<={self.value[1]}'

