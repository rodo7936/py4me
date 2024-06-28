from typing import Any


class Filter:
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value

    def as_param(self) -> dict:
        ...


class GreaterThanFilter(Filter):
    """
    Filter for checking if field is greater than value
    """

    def as_param(self):
        return {self.field: f'>{self.value}'}


class LessThanFilter(Filter):
    """
    Filter for checking if field is less than value
    """

    def as_param(self):
        return {self.field: f'<{self.value}'}


class EqualFilter(Filter):
    """
    Filter for checking if field is equal to value
    """

    def as_param(self):
        return {self.field: str(self.value)}


class NotEqualFilter(Filter):
    """
    Filter for checking if field is not equal to value
    """

    def as_param(self):
        return {self.field: f'!{self.value}'}


class GreaterOrEqualFilter(Filter):
    """
    Filter for checking if field is greater or equal to value
    """

    def as_param(self):
        return {self.field: f'>={self.value}'}


class LessOrEqualFilter(Filter):
    """
    Filter for checking if field is less or equal to value
    """

    def as_param(self):
        return {self.field: f'<={self.value}'}


class PresentFilter(Filter):
    """
    Filter for checking if field is present and contains value
    """

    def as_param(self):
        return {self.field: '!'}


class EmptyFilter(Filter):
    """
    Filter for checking if field is empty
    """

    def as_param(self):
        return {self.field: ''}


class NotInFilter(Filter):
    """
    Filter for checking if field is not in list of values
    """

    def as_param(self):
        if isinstance(self.value, (list, tuple, set)):
            return {self.field: f'!{",".join([str(v) for v in self.value])}'}
        if isinstance(self.value, str):
            return {self.field: f'!{self.value}'}


class InFilter(Filter):
    """
    Filter for checking if field is in list of values
    """

    def as_param(self):
        if isinstance(self.value, (list, tuple, set)):
            return {self.field: f'{",".join(self.value)}'}
        if isinstance(self.value, str):
            return {self.field: f'{self.value}'}


class GreaterThanLessThanFilter(Filter):
    """
    Filter for checking if field is greater than value and less than value
    """

    def as_param(self):
        if not isinstance(self.value, (list, tuple, set)):
            raise ValueError('Value must be an list, tuple or set')
        return {self.field: '>{}<{}'.format(self.value[0], self.value[1])}


class GreaterEqualLessEqualFilter(Filter):
    """
    Filter for checking if field is greater or equal to value and less or equal to value
    """

    def as_param(self):
        if not isinstance(self.value, (list, tuple, set)):
            raise ValueError('Value must be an list, tuple or set')
        return {self.field: '>={}<={}'.format(self.value[0], self.value[1])}
