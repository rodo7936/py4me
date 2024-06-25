from enum import Enum
from src.exceptions import (InvalidEnvironmentException,
                            InvalidRegionException,
                            )
from abc import ABC, abstractmethod


class Py4meUrl:
    def __init__(self, env, region):
        self.env = env
        self.region = region

    def _region_part(self):
        if self.region.value == 'global':
            return ''
        return f'{self.region.value}.'

    def _env_part(self):
        if self.env.value == 'qa':
            return '.qa/v1'
        return '.com/v1'

    def _check_demo(self):
        return self.env.value == 'demo'

    def create(self):
        if self._check_demo():
            return 'https://api.4me-demo.com/v1'
        return f'https://api.{self._region_part()}4me{self._env_part()}'


class Environment(str, Enum):
    PROD = 'prod'
    QA = 'qa'
    DEMO = 'demo'

    @classmethod
    def check_valid(cls, value):
        if value.lower() not in cls.__members__.values():
            raise InvalidEnvironmentException(f'Invalid environment: {value}. '
                                              f'Valid environments are: {list(cls.__members__.values())}')
        return cls(value)


class Region(str, Enum):
    GLOBAL = 'global'
    AUSTRALIA = 'au'
    UNITED_STATES = 'us'
    UNITED_KINGDOM = 'uk'
    SWITZERLAND = 'ch'

    @classmethod
    def check_valid(cls, value):
        if value.lower() not in cls.__members__.values():
            raise InvalidRegionException(f'Invalid region: {value}. '
                                         f'Valid regions are: {list(cls.__members__.values())}.')
        return cls(value)



class Auth(ABC):

    @abstractmethod
    def get_token(self) -> str:
        ...

    def get_account(self) -> str:
        ...









