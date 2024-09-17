import unittest

from py4me.organizations.models import Organization
from py4me.organizations.organizations_api import OrganizationsApi

class TestOrganization(unittest.TestCase):
    def test_organization_api(self):
        api = OrganizationsApi(url='url', token='token', account='account')
        self.assertEqual(api.model, Organization)

    def test_predefined_filters_include_all_expected_values(self):
        expected_filters = [
            'disabled',
            'enabled',
            'external',
            'internal',
            'trusted',
            'directory',
            'support_domain',
            'managed_by_me'
        ]
        self.assertListEqual(OrganizationsApi.avaiable_predefined_filters, expected_filters)

    def test_predefined_filters_do_not_include_unexpected_values(self):
        unexpected_filters = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for filter_ in unexpected_filters:
            self.assertNotIn(filter_, OrganizationsApi.avaiable_predefined_filters)

    def test_predefined_filters_are_unique(self):
        filters = OrganizationsApi.avaiable_predefined_filters
        self.assertEqual(len(filters), len(set(filters)))

    def test_sortable_fields_include_all_expected_values(self):
        expected_fields = [
            'id',
            'sourceID',
            'name',
            'parent',
            'manager',
            'created_at',
            'updated_at'
        ]
        self.assertListEqual(OrganizationsApi.sortable_fields, expected_fields)

    def stest_ortable_fields_do_not_include_unexpected_values(self):
        unexpected_fields = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for field in unexpected_fields:
            self.assertNotIn(field, OrganizationsApi.sortable_fields)

    def test_sortable_fields_are_unique(self):
        fields = OrganizationsApi.sortable_fields
        self.assertEqual(len(fields), len(set(fields)))

    def test_filtering_fields_include_all_expected_values(self):
        expected_fields = [
            'id',
            'source',
            'sourceID',
            'name',
            'disabled',
            'created_at',
            'updated_at',
            'financialID',
            'parent',
        ]
        self.assertListEqual(OrganizationsApi.filtering_fields, expected_fields)

    def test_filtering_fields_do_not_include_unexpected_values(self):
        unexpected_fields = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for field in unexpected_fields:
            self.assertNotIn(field, OrganizationsApi.filtering_fields)

    def test_filtering_fields_are_unique(self):
        fields = OrganizationsApi.filtering_fields
        self.assertEqual(len(fields), len(set(fields)))