import unittest

from py4me.requests.models import Request
from py4me.requests.requests_api import RequestApi

class TestRequestApi(unittest.TestCase):
    def test_predefined_filters_include_all_expected_values(self):
        expected_filters = [
            'completed',
            'open',
            'requested_by_or_for_me',
            'assigned_to_my_team',
            'assigned_to_me',
            'waiting_for_me',
            'problem_management_review',
            'sla_accountability'
        ]
        self.assertListEqual(RequestApi.avaiable_predefined_filters, expected_filters)

    def test_predefined_filters_do_not_include_unexpected_values(self):
        unexpected_filters = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for filter_ in unexpected_filters:
            self.assertNotIn(filter_, RequestApi.avaiable_predefined_filters)

    def test_predefined_filters_are_unique(self):
        filters = RequestApi.avaiable_predefined_filters
        self.assertEqual(len(filters), len(set(filters)))

    def test_sortable_fields_include_all_expected_values(self):
        expected_fields = [
            'id',
            'sourceID',
            'subject',
            'category',
            'impact',
            'status',
            'next_target_at',
            'completed_at',
            'team',
            'member',
            'service_instance',
            'created_at',
            'updated_at'
        ]
        self.assertListEqual(RequestApi.sortable_fields, expected_fields)

    def test_sortable_fields_do_not_include_unexpected_values(self):
        unexpected_fields = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for field in unexpected_fields:
            self.assertNotIn(field, RequestApi.sortable_fields)

    def test_sortable_fields_are_unique(self):
        fields = RequestApi.sortable_fields
        self.assertEqual(len(fields), len(set(fields)))

    def test_filtering_fields_include_all_expected_values(self):
        expected_fields = [
            'id',
            'source',
            'sourceID',
            'subject',
            'category',
            'impact',
            'status',
            'workflow',
            'next_target_at',
            'completed_at',
            'created_by',
            'grouping',
            'grouped_into',
            'knowledge_article',
            'requested_by',
            'requested_for',
            'service_instance',
            'supplier_requestID',
            'created_at',
            'updated_at',
            'team',
            'member',
            'template',
            'major_incident_status',
            'Request'
        ]
        self.assertListEqual(RequestApi.filtering_fields, expected_fields)

    def test_filtering_fields_do_not_include_unexpected_values(self):
        unexpected_fields = [
            'unknown',
            'invalid',
            'unsupported'
        ]
        for field in unexpected_fields:
            self.assertNotIn(field, RequestApi.filtering_fields)

    def test_filtering_fields_are_unique(self):
        fields = RequestApi.filtering_fields
        self.assertEqual(len(fields), len(set(fields)))