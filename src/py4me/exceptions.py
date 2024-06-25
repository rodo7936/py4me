class Py4MeError(Exception):
    """Base class for all exceptions in Py4Me."""
    ...


class ValidationError(Py4MeError):
    ...


class InvalidEnvironmentException(Py4MeError):
    ...


class InvalidRegionException(Py4MeError):
    ...


class BadFilterException(Py4MeError):
    ...


class BadSortFieldException(Py4MeError):
    ...


class InvalidUrlException(Py4MeError):
    ...


class InvalidTokenException(Py4MeError):
    ...


class ApiError(Py4MeError):
    ...


class TooManyRequestsException(Py4MeError):
    ...


class ObjectNotFound(Py4MeError):
    ...


class SemanticException(Py4MeError):
    ...
