import unittest

from py4me.filters import Filter, EqualFilter, GreaterThanFilter, LessThanFilter, NotEqualFilter, \
    GreaterOrEqualFilter, LessOrEqualFilter, PresentFilter, EmptyFilter, NotInFilter, InFilter, \
    GreaterThanLessThanFilter, GreaterEqualLessEqualFilter


class TestFilter(unittest.TestCase):

    def test_filter_init(self):
        filter = Filter(field='', value='')
        self.assertIsInstance(filter, Filter)

    def test_gt_filter(self):
        filter = GreaterThanFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '>value'})

    def test_lt_filter(self):
        filter = LessThanFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '<value'})

    def test_eq_filter(self):
        filter = EqualFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': 'value'})

    def test_ne_filter(self):
        filter = NotEqualFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '!value'})

    def test_ge_filter(self):
        filter = GreaterOrEqualFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '>=value'})

    def test_le_filter(self):
        filter = LessOrEqualFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '<=value'})

    def test_present_filter(self):
        filter = PresentFilter(field='field', value='')
        self.assertEqual(filter.as_param(), {'field': '!'})

    def test_empty_filter(self):
        filter = EmptyFilter(field='field', value='')
        self.assertEqual(filter.as_param(), {'field': ''})

    def test_not_in_filter(self):
        filter = NotInFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': '!value'})

    def test_not_in_filter_iter(self):
        filter = NotInFilter(field='field', value=['value1', 'value2'])
        self.assertEqual(filter.as_param(), {'field': '!value1,value2'})

    def test_in_filter(self):
        filter = InFilter(field='field', value='value')
        self.assertEqual(filter.as_param(), {'field': 'value'})

    def test_in_filter_iter(self):
        filter = InFilter(field='field', value=['value1', 'value2'])
        self.assertEqual(filter.as_param(), {'field': 'value1,value2'})

    def test_gt_lt_filter(self):
        filter = GreaterThanLessThanFilter(field='field', value=['value1', 'value2'])
        self.assertEqual(filter.as_param(), {'field': '>value1<value2'})

    def test_gt_lt_filter_single(self):
        with self.assertRaises(ValueError):
            GreaterThanLessThanFilter(field='field', value='value').as_param()

    def test_ge_le_filter(self):
        filter = GreaterEqualLessEqualFilter(field='field', value=['value1', 'value2'])
        self.assertEqual(filter.as_param(), {'field': '>=value1<=value2'})

    def test_ge_le_filter_single(self):
        with self.assertRaises(ValueError):
            GreaterEqualLessEqualFilter(field='field', value='value').as_param()


if __name__ == '__main__':
    unittest.main()
