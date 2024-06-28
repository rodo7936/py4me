import unittest

from py4me.auth.auth import PATAuth
from py4me.exceptions import InvalidEnvironmentException, InvalidRegionException
from py4me.py4me import Connection, Environment, Py4meUrl, Region


class TestConnection(unittest.TestCase):
    def test_connection(self):
        conn = Connection(region='us', environment='prod', auth=PATAuth('', ''))
        self.assertIsInstance(conn, Connection)


class TestEnvironment(unittest.TestCase):

    def test_valid(self):
        env = Environment.check_valid('prod')
        self.assertEqual(env, Environment.PROD)

    def test_invalid(self):
        with self.assertRaises(InvalidEnvironmentException):
            Environment.check_valid('invalid')


class TestPy4MeUrl(unittest.TestCase):
    def setUp(self):
        self.dummy_auth = PATAuth('', '')

    def test_create_global_qa_environment(self):
        py4me_url = Py4meUrl(Environment.QA, Region.GLOBAL)
        result = py4me_url.create()
        self.assertEqual(result, "https://api.4me.qa/v1")

    def test_create_australia_demo_environment(self):
        py4me_url = Py4meUrl(Environment.DEMO, Region.AUSTRALIA)
        result = py4me_url.create()
        self.assertEqual(result, "https://api.4me-demo.com/v1")

    def test_create_invalid_environment(self):
        with self.assertRaises(InvalidEnvironmentException):
            Py4meUrl('invalid', Region.GLOBAL)

    def test_create_invalid_region(self):
        with self.assertRaises(InvalidRegionException):
            Py4meUrl(Environment.QA, 'invalid')

    def test_change_environment(self):
        conn = Connection(region='us', environment='prod', auth=self.dummy_auth)
        conn.change_environment('qa')
        self.assertEqual(conn._environment, Environment.QA)

    def test_change_region(self):
        conn = Connection(region='us', environment='prod', auth=self.dummy_auth)
        conn.change_region('uk')
        self.assertEqual(conn._region, Region.UNITED_KINGDOM)



if __name__ == '__main__':
    unittest.main()
