from abc import ABC

from requests import get as get_, patch as patch_, post as post_, put as put_

from py4me.exceptions import (BadFilterException, BadSortFieldException, InvalidUrlException,
                              InvalidTokenException, ObjectNotFound, SemanticException, TooManyRequestsException,
                              ApiError)
from py4me.filters import Filter


class ListMethodBuilder:
    def __init__(self, raw_uri: str,
                 fields: list[str] = None,
                 predefined_filter: str | None = None,
                 filters: list[Filter] | None = None,
                 sort: str | None = None):
        self.fields = fields
        self.sort = sort
        self.filters = filters
        self.predefined_filter = predefined_filter
        self.raw_uri = raw_uri
        self.uri = self.raw_uri
        self._params = {'per_page': 100}

    def _predefined_uri(self):
        return f'{self.raw_uri}/{self.predefined_filter}'

    def _sort_uri(self):
        if self.sort:
            self._params['sort'] = self.sort

    def _fields_uri(self):
        if self.fields:
            self._params['fields'] = ','.join(self.fields)

    def _filters_uri(self):
        if self.filters:
            for _ in self.filters:
                self._params.update(_.as_param())

    def get(self):
        if self.predefined_filter:
            self.uri = self._predefined_uri()
        self._sort_uri()
        self._fields_uri()
        self._filters_uri()
        return self.uri, self._params


class StatusCodeHandler:
    def __init__(self, response):
        self.response = response
        self.sc = response.status_code
        self.json = response.json()

    def _response_as_text(self):
        return f"{self.json.get('message')}: {self.json.get('errors') if self.json.get('errors') else ''}"

    def run(self):
        if self.sc == 200:
            return self.response
        elif self.sc == 201:
            return self.response
        elif self.sc == 204:
            return self.response
        elif self.sc == 400:
            raise InvalidUrlException(self._response_as_text())
        elif self.sc == 401:
            raise InvalidTokenException((self._response_as_text()))
        elif self.sc == 404:
            raise ObjectNotFound((self._response_as_text()))
        elif self.sc == 422:
            raise SemanticException((self._response_as_text()))
        elif self.sc == 429:
            raise TooManyRequestsException((self._response_as_text()))
        else:
            raise ApiError((self._response_as_text()))


class Api(ABC):
    avaiable_predefined_filters = []
    sortable_fields = []
    collection_fields = []
    filtering_fields = []
    model = None

    def __init__(self, url: str, endpoint: str, token: str, account: str = None):
        self.uri = f'{url}/{endpoint}'
        self.__token, self.__account = token, account
        self.header = self.__create_header()

    def __create_header(self) -> dict:
        return {
            'Authorization': f'Bearer {self.__token}',
            'X-4me-Account': self.__account
        }

    def list(self,
             fields: list[str] = None,
             predefined_filter: str | None = None,
             filters: list | None = None,
             sort: str | None = None
             ):
        if predefined_filter and predefined_filter.lower() not in self.avaiable_predefined_filters:
            raise BadFilterException(f'Predefined filter {predefined_filter} is not available for this endpoint.')
        if sort and sort.lower() not in self.sortable_fields:
            raise BadSortFieldException(f'Sort field {sort} is not available for this endpoint.')
        if fields:
            if not all([field.lower() in self.collection_fields for field in fields]):
                raise BadFilterException(f'Fields {fields} are not available for this endpoint.')
        if predefined_filter and filters:
            raise BadFilterException('You can not use predefined filter and filters at the same time.')
        uri, params = ListMethodBuilder(raw_uri=self.uri,
                                        fields=fields,
                                        predefined_filter=predefined_filter,
                                        filters=filters,
                                        sort=sort).get()
        _retr = []
        while True:
            response = StatusCodeHandler(get_(url=uri,
                                              headers=self.header,
                                              params=params) if not _retr else get_(url=uri,
                                                                                    headers=self.header)).run()
            _retr.extend(response.json())
            if 'next' not in response.links:
                break
            uri = response.links.get('next').get('url')
        return _retr

    def get(self, id_: int):
        response = StatusCodeHandler(get_(url=f'{self.uri}/{id_}',
                                          headers=self.header)).run()
        return response.json()

    def create(self, data: dict):
        response = StatusCodeHandler(post_(url=self.uri,
                                           headers=self.header,
                                           json=data)).run()
        return response.json()

    def update(self, id_: int, data: dict):
        response = StatusCodeHandler(patch_(url=f'{self.uri}/{id_}',
                                            headers=self.header,
                                            json=data)).run()
        return response.json()

    def update_create(self, id_: int, data: dict):
        response = StatusCodeHandler(put_(url=f'{self.uri}/{id_}',
                                          headers=self.header,
                                          json=data)).run()
        return response.json()
