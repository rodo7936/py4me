from enum import Enum

from py4me.auth.auth import Auth
from py4me.exceptions import InvalidEnvironmentException, InvalidRegionException
from py4me.people.people_api import PeopleApi


class Py4meUrl:
    def __init__(self, env, region):
        self.env = Environment.check_valid(env)
        self.region = Region.check_valid(region)

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


class Connection:
    _auth: Auth | None = None
    people = ...
    requests = ...
    tasks = ...
    organizations = ...

    def __init__(self, environment: Environment | str, region: Region | str, auth: Auth):
        self._environment = Environment.check_valid(environment)
        self._region = Region.check_valid(region)
        self.__url = self._create_url()
        self._auth = auth
        self.__change_connections()

    def __change_connections(self):
        self.people = PeopleApi(self.__url, self._auth.get_token, self._auth.get_account)
        self.requests = ...
        self.tasks = ...
        self.accounts = ...

    def _create_url(self):
        return Py4meUrl(self._environment, self._region).create()

    def change_environment(self, environment: Environment):
        self._environment = Environment.check_valid(environment)
        self.__url = self._create_url()
        self.__change_connections()

    def change_region(self, region: Region):
        self._region = Region.check_valid(region)
        self.__url = self._create_url()
        self.__change_connections()
