from py4me.serialization import Model
from datetime import datetime as dt


class Request(Model):
    _fields = {
        'addressed': bool,
        'agile_board': 'AgileBoard',
        'agile_board_column': 'AgileBoardColumn',
        'agile_board_column_position': int,
        'assignment_count': int,
        'attachments': list['Attachment'],
        'category': 'RequestCategory',
        'ci': 'ConfigurationItem',
        'checked_items': list[str],
        'completed_at': dt,
        'completion_reason': 'RequestCompletionReason',
        'created_at': dt,
        'created_by': 'Person',
        'custom_fields': list['CustomField'],
        'custom_fields_attachments': list['Attachment'],
        'downtime_end_at': dt,
        'downtime_start_at': dt,
        'desired_completion_at': dt,
        'feedback': 'RequestFeedback',
        'grouped_into': 'Request',
        'grouping': 'RequestGrouping',
        'id': int,
        'impact': 'RequestImpact',
        'internal_note': str,
        'internal_note_attachments': list['Attachment'],
        'knowledge_article': 'KnowledgeArticle',
        'major_incident_status': 'MajorIncidentStatus',
        'member': 'Person',
        'new_assignment': bool,
        'next_target_at': dt,
        'note': str,
        'note_attachments': list['Attachment'],
        'organization': 'Organization',
        'planned_effort': int,

    }
    _required_fields = {
        'category': 'RequestCategory',
    }

    _readonly_fields = {
        'assignment_count': int,
        'attachments': list['Attachment'],
        'completed_at': dt,
        'created_at': dt,
        'created_by': 'Person',
        'feedback': 'RequestFeedback',
        'grouping': 'RequestGrouping',
        'id': int,
        'new_assignment': bool,
        'next_target_at': dt,
        'organization': 'Organization',
    }

    _validation = {
    }
