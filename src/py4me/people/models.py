from datetime import datetime as dt

# from src.py4me.other_models.address import Address
from src.py4me.serialization import Model


class Person(Model):
    _fields = {
        'account': 'Account',
        'nodeID': str,
        'authenticationID': str,
        'auto_translation': bool,
        'cost_per_hour': float,
        'cost_per_hour_currency': 'Currency',
        'custom_fields': list['CustomField'],
        'custom_fields_attachments': list['Attachment'],
        'disabled': bool,
        'do_not_translate_languages': str,
        'employeeID': str,
        'exclude_team_notifications': bool,
        'guest': bool,
        'information': str,
        'information_attachments': list['Attachment'],
        'job_title': str,
        'locale': str,
        'location': str,
        'manager': 'Person',
        'oauth_person_enablement': bool,
        'organization': 'Organization',
        'picture_uri': str,
        'send_email_notifications': 'NotificationEnum',
        'show_notification_popup': 'NotificationEnum',
        'site': 'Site',
        'source': str,
        'sourceID': str,
        'supportID': str,
        'time_format_24h': bool,
        'time_zone': 'TimeZone',
        'vip': bool,
        'work_hours': 'Calendar',
        'name': str,
        'primary_email': str,
        'addresses': list['Address'],
        'id': int,
        'created_at': dt,
        'updated_at': dt,
        'attachments': list['Attachment'],
        'contacts': list['Contact'],
        'ui_extension': 'UiExtension',
        'color_mode': str,  # non_prod: Pre-prod only
        'formats': str,  # non_prod: Pre-prod only
        'play_private_chat_sound':  str,  # non_prod: Pre-prod only
        'play_support_chat_sound': str,  # non_prod: Pre-prod only
        'show_private_chat_popup': str,  # non_prod: Pre-prod only
        'show_support_chat_popup': str,  # non_prod: Pre-prod only

    }

    _required_fields = {
        'name': str,
        'primary_email': str,

    }
    _readonly_fields = {
        'addresses': list['Address'],
        'id': int,
        'created_at': dt,
        'updated_at': dt,
        'attachments': list['Attachment'],
        'contacts': list['Contact'],
        'ui_extension': 'UiExtension',
        'account': 'Account',
        'nodeID': str,
    }

    _validation = {
        'authenticationID': {'max_length': 128},
        'employeeID': {'max_length': 128},
        'job_title': {'max_length': 80},
        'locale': {'max_length': 5},
        'location': {'max_length': 80},
        'name': {'max_length': 128},
        #            'information': {'max_length': 1024},  Teorically the max is 64kb, but we can't validate this
    }


# Address, Attachment, Currency, Contact, CustomField, NotificationEnum, Organization, Site, TimeZone, UiExtension
