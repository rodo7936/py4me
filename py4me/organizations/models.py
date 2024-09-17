from datetime import datetime

from py4me.other_models.custom_field import CustomField
from py4me.serialization import Model


class Organization(Model):
    _fields = {
        'business_unit': bool,
        'custom_fields': list[CustomField],
        'custom_fields_attachments': list['Attachment'],
        'disabled': bool,
        'end_user_privacy': bool,
        'financialID': str,
        'manager': 'Person',
        'parent': 'Organization',
        'picture_uri': str,
        'region': str,
        'remarks': str,
        'remarks_attachments': list['Attachment'],
        'source': str,
        'sourceID': str,
        'substitute': 'Person',
        'addresses': list['Address'],
        'attachments': list['Attachment'],
        'business_unit_reference': 'Organization',
        'contacts': list['Contact'],
        'created_at': datetime,
        'ui_extension': 'UiExtension',
        'updated_at': datetime,
        'name': str,
        'order_template': 'RequestTemplate',
    }
    _required_fields = {
        'name': str,
        'order_template': 'RequestTemplate',
    }

    _readonly_fields = {
        'id': int,
        'addresses': list['Address'],
        'attachments': list['Attachment'],
        'business_unit_reference': 'Organization',
        'contacts': list['Contact'],
        'created_at': datetime,
        'ui_extension': 'UiExtension',
        'updated_at': datetime,
        }

    _validation = {

        }
