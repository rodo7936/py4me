from py4me._api.py4me_api import Api
from py4me.organizations.models import Organization


class OrganizationApi(Api):
    model = Organization
    avaiable_predefined_filters = [
        'completed',
        'open',
        'requested_by_or_for_me',
        'assigned_to_my_team',
        'assigned_to_me',
        'waiting_for_me',
        'problem_management_review',
        'sla_accountability'
    ]
    sortable_fields = [
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
    collection_fields = model.model_fields

    filtering_fields = [
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
        'organization'
    ]

    def __init__(self, url: str, token: str, account: str) -> None:
        super().__init__(
            url=url,
            token=token,
            account=account,
            endpoint='organizations',
        )

    def create(self, model: Organization) -> Organization:
        model = model.deserialize()
        return Organization.serialize(**super().create(model))

    def list(
            self,
            fields: list[str] = None,
            predefined_filter: str | None = None,
            filters: list | None = None,
            sort: str | None = None
    ):
        return [Organization.serialize(**o) for o in super().list(fields, predefined_filter, filters, sort)]

    def get(self, id_: int) -> Organization:
        return Organization.serialize(**super().get(id_))

    def update(self, model: Organization) -> Organization:
        deserialized = model.deserialize()
        return Organization.serialize(**super().update(id_=model.id, data=deserialized))
