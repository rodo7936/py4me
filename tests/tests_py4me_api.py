import unittest
from unittest.mock import Mock, patch

from py4me._api.py4me_api import ListMethodBuilder, StatusCodeHandler, Api
from py4me.exceptions import InvalidUrlException, InvalidTokenException, SemanticException, \
    TooManyRequestsException, ApiError, BadFilterException, BadSortFieldException
from py4me.filters import EqualFilter


class TestListMethodBuilder(unittest.TestCase):

    def test_deafault_param(self):
        builder = ListMethodBuilder('test')
        self.assertIsNone(builder.fields)
        self.assertIsNone(builder.sort)
        self.assertIsNone(builder.filters)
        self.assertIsNone(builder.predefined_filter)
        self.assertEqual(builder.raw_uri, 'test')
        self.assertEqual(builder.uri, 'test')
        self.assertEqual(builder._params, {'per_page': 100})

    def test_predefined_uri(self):
        builder = ListMethodBuilder('test', predefined_filter='disabled')
        self.assertEqual(builder._predefined_uri(), 'test/disabled')

    def test_sort_uri(self):
        builder = ListMethodBuilder('test', sort='name')
        builder._sort_uri()
        self.assertEqual(builder._params, {'per_page': 100, 'sort': 'name'})

    def test_fields_uri(self):
        builder = ListMethodBuilder('test', fields=['name', 'email'])
        builder._fields_uri()
        self.assertEqual(builder._params, {'per_page': 100, 'fields': 'name,email'})

    def test_filters_uri(self):
        builder = ListMethodBuilder('test', filters=[EqualFilter(field='name', value='test')])
        builder._filters_uri()
        self.assertEqual(builder._params, {'per_page': 100, 'name': 'test'})

    def test_get(self):
        builder = ListMethodBuilder('test', fields=['name', 'email'], predefined_filter='disabled', sort='name')
        uri, params = builder.get()
        self.assertEqual(uri, 'test/disabled')
        self.assertEqual(params, {'per_page': 100, 'fields': 'name,email', 'sort': 'name'})


class TestStatusHandler(unittest.TestCase):

    def test_response_as_text(self):
        response = Mock()
        response.status_code = 400
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        self.assertEqual(handler._response_as_text(), 'test: error')

    def test_run_200(self):
        response = Mock()
        response.status_code = 200
        handler = StatusCodeHandler(response)
        self.assertEqual(handler.run(), response)

    def test_run_201(self):
        response = Mock()
        response.status_code = 201
        handler = StatusCodeHandler(response)
        self.assertEqual(handler.run(), response)

    def test_run_204(self):
        response = Mock()
        response.status_code = 204
        handler = StatusCodeHandler(response)
        self.assertEqual(handler.run(), response)

    def test_run_400(self):
        response = Mock()
        response.status_code = 400
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        with self.assertRaises(InvalidUrlException):
            handler.run()

    def test_run_401(self):
        response = Mock()
        response.status_code = 401
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        with self.assertRaises(InvalidTokenException):
            handler.run()

    def test_run_422(self):
        response = Mock()
        response.status_code = 422
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        with self.assertRaises(SemanticException):
            handler.run()

    def test_run_429(self):
        response = Mock()
        response.status_code = 429
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        with self.assertRaises(TooManyRequestsException):
            handler.run()

    def test_run_default(self):
        response = Mock()
        response.status_code = 500
        response.json.return_value = {'message': 'test', 'errors': 'error'}
        handler = StatusCodeHandler(response)
        with self.assertRaises(ApiError):
            handler.run()


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Api(account='test', endpoint='test', token='test', url='https://api.4me.com')

    def test_url(self):
        self.assertEqual(self.api.uri, 'https://api.4me.com/test')

    def test_header(self):
        self.assertEqual(self.api.header, {'Authorization': 'Bearer test', 'X-4me-Account': 'test'})

    @patch('py4me._api.py4me_api.get_')
    def test_list_predefined_filter(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        self.api.avaiable_predefined_filters = ['disabled']
        self.api.list(predefined_filter='disabled')
        mock_get.assert_called_once_with(url='https://api.4me.com/test/disabled',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         params={'per_page': 100})

    @patch('py4me._api.py4me_api.get_')
    def test_list_predefined_filter_non_avaiable(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        with self.assertRaises(BadFilterException):
            self.api.list(predefined_filter='disabled')

    @patch('py4me._api.py4me_api.get_')
    def test_list_sort(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        self.api.sortable_fields = ['name']
        self.api.list(sort='name')
        mock_get.assert_called_once_with(url='https://api.4me.com/test',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         params={'per_page': 100, 'sort': 'name'})

    @patch('py4me._api.py4me_api.get_')
    def test_list_sort_non_avaiable(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        with self.assertRaises(BadSortFieldException):
            self.api.list(sort='name')

    @patch('py4me._api.py4me_api.get_')
    def test_list_fields(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        self.api.collection_fields = ['name']
        self.api.list(fields=['name'])
        mock_get.assert_called_once_with(url='https://api.4me.com/test',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         params={'per_page': 100, 'fields': 'name'})

    @patch('py4me._api.py4me_api.get_')
    def test_list_fields_non_avaiable(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        with self.assertRaises(BadFilterException):
            self.api.list(fields=['name'])

    @patch('py4me._api.py4me_api.get_')
    def test_list_predefined_filter_and_filters(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        self.api.collection_fields = ['name']
        self.api.avaiable_predefined_filters = ['disabled']
        with self.assertRaises(BadFilterException):
            self.api.list(predefined_filter='disabled', filters=[EqualFilter(field='name', value='test')])

    @patch('py4me._api.py4me_api.get_')
    def test_get(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_get.return_value = response
        self.api.get(1)
        mock_get.assert_called_once_with(url='https://api.4me.com/test/1',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'})

    @patch('py4me._api.py4me_api.post_')
    def test_post(self, mock_post):
        response = Mock()
        response.status_code = 201
        response.json.return_value = {'data': []}
        response.links = {}
        mock_post.return_value = response
        self.api.create({'data': 'test'})
        mock_post.assert_called_once_with(url='https://api.4me.com/test',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         json={'data': 'test'})

    @patch('py4me._api.py4me_api.patch_')
    def test_patch(self, mock_patch):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_patch.return_value = response
        self.api.update(1, {'data': 'test'})
        mock_patch.assert_called_once_with(url='https://api.4me.com/test/1',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         json={'data': 'test'})

    @patch('py4me._api.py4me_api.put_')
    def test_put(self, mock_put):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'data': []}
        response.links = {}
        mock_put.return_value = response
        self.api.update_create(1, {'data': 'test'})
        mock_put.assert_called_once_with(url='https://api.4me.com/test/1',
                                         headers={'Authorization': 'Bearer test', 'X-4me-Account': 'test'},
                                         json={'data': 'test'})


if __name__ == '__main__':
    unittest.main()
