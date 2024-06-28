from py4me.organizations.models import Organization
from py4me._api.py4me_api import Api


class OrganizationApi(Api):
    model = Organization
    avaiable_predefined_filters = [
        'disabled',
        'enabled',
        'external',
        'internal',
        'trusted',
        'directory',
        'support_domain'
        'managed_by_me',
    ]
    sortable_fields = [
        'id',
        'sourceID',
        'name',
        'created_at',
        'updated_at',
    ]
    filtering_fields = [
        'id',
        'source',
        'sourceID',
        'name',
        'disabled',
        'created_at',
        'updated_at',
        'disabled',
        'financialID',
        'parent'
    ]
    collection_fields = model.model_fields

    def __init__(self):
        super().__init__(
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
    ) -> list[Organization]:
        return [Organization.serialize(**o) for o in super().list(fields, predefined_filter, filters, sort)]

    def get(self, id_: int) -> Organization:
        return Organization.serialize(**super().get(id_))

    def update(self, model: Organization) -> Organization:
        model = model.deserialize()
        return Organization.serialize(**super().update(model.id, model))