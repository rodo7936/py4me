from utils import Auth, Environment, Region, Py4meUrl
from src.api import OrganizationsApi
from src.api import PeopleApi


class PATAuth(Auth):
    def __init__(self, token: str, account):
        self.account = account
        self.token = token

    def get_token(self) -> str:
        return self.token

    def get_account(self) -> str:
        return self.account


class OAuth2Auth(Auth):
    def __init__(self, token):
        self.token = token
        raise NotImplementedError('OAuth2Auth is not implemented yet.')

    def get_token(self) -> str:
        return self.token


class Connection:
    _auth: Auth | None = None
    people = PeopleApi
    requests = ...
    tasks = ...
    organizations = OrganizationsApi
    accounts = ...

    def __init__(self, environment: Environment | str, region: Region | str, auth: Auth):
        self._environment = Environment.check_valid(environment)
        self._region = Region.check_valid(region)
        self.__url = self._create_url()
        self._auth = auth
        self.__change_connections()

    def __change_connections(self):
        self.organizations = OrganizationsApi(self.__url, self._auth.get_token(), self._auth.get_account())
        self.people = PeopleApi(self.__url, self._auth.get_token(), self._auth.get_account())
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
