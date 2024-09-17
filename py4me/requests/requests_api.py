from py4me._api.py4me_api import Api
from py4me.requests.models import Request


class RequestApi(Api):
    model = Request
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
        'Request'
    ]

    def __init__(self, url: str, token: str, account: str) -> None:
        super().__init__(
            url=url,
            token=token,
            account=account,
            endpoint='requests',
        )

    def create(self, model: Request) -> Request:
        model = model.deserialize()
        return Request.serialize(**super().create(model))

    def list(
            self,
            fields: list[str] = None,
            predefined_filter: str | None = None,
            filters: list | None = None,
            sort: str | None = None
    ):
        return [Request.serialize(**r) for r in super().list(fields, predefined_filter, filters, sort)]

    def get(self, id_: int) -> Request:
        return Request.serialize(**super().get(id_))

    def update(self, model: Request) -> Request:
        deserialized = model.deserialize()
        return Request.serialize(**super().update(id_=model.id, data=deserialized))
