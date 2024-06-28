from py4me.serialization import Model


class Account(Model):
    _fields = {
        'currency': 'Currency',
        'directory_account': 'Account',
        'id': str,
        'locale': 'Locale',
        'name': str,
        'organization': 'Organization',
        'owner': 'Person',
        'plan': 'Plan',
        'strong_privacy': bool,
        'time_format_24h': bool,
        'url': str,
    }

    _required_fields = {
        'plan': 'Plan',
        'owner': 'Person',
        'name': str,
        'locale': 'Locale',
        'currency': 'Currency',
    }

    _readonly_fields = {
        'id': str,
        'organization': 'Organization',
        'url': str,
    }

    _validation = {

    }