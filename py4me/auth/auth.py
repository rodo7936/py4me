from abc import ABC, abstractmethod


class Auth(ABC):

    @property
    @abstractmethod
    def get_token(self) -> str:
        ...

    @property
    @abstractmethod
    def get_account(self) -> str:
        ...


class PATAuth(Auth):
    def __init__(self, token: str, account):
        self.account = account
        self.token = token

    @property
    def get_token(self) -> str:
        return self.token

    @property
    def get_account(self) -> str:
        return self.account


class OAuth2Auth(Auth):
    def __init__(self, token):
        self.token = token
        raise NotImplementedError('OAuth2Auth is not implemented yet.')

    @property
    def get_account(self) -> str:
        return ...

    @property
    def get_token(self) -> str:
        return self.token
