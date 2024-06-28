from py4me.serialization import Model
from datetime import datetime as dt


class Organization(Model):
    _fields = {
        'addresses': list['Address'],
        'attachments': list['Attachment'],
        'business_unit': bool,
        'business_unit_organization': 'Organization',
        'contacts': list['Contact'],
        'created_at': dt,
        'custom_fields': list['CustomField'],
        'custom_fields_attachments': list['Attachment'],
        'disabled': bool,
        'financialID': str,
        'id': int,
        'manager': 'Person',
        'name': str,
        'order_template': 'RequestTemplate',
        'parent': 'Organization',
        'picture_uri': str,
        'region': str,
        'remarks': str,
        'remarks_attachments': list['Attachment'],
        'source': str,
        'sourceID': str,
        'substitute': 'Person',
        'ui_extension': 'UiExtension',
        'updated_at': dt,
    }
    _required_fields = {
        'name': str,
        'order_template': 'RequestTemplate'
    }

    _readonly_fields = {
        'addresses': list['Address'],
        'attachments': list['Attachment'],
        'business_unit_organization': 'Organization',
        'contacts': list['Contact'],
        'created_at': dt,
        'id': int,
        'ui_extension': 'UiExtension',
        'updated_at': dt,
    }

    _validation = {

    }
