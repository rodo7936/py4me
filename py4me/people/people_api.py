from py4me._api.py4me_api import Api
from py4me.people.models import Person


class PeopleApi(Api):
    model = Person
    avaiable_predefined_filters = [
        'disabled',
        'enabled',
        'internal',
        'directory',
        'support_domain'
    ]
    sortable_fields = [
        'id',
        'sourceID',
        'name',
        'organization',
        'site',
        'manager',
        'created_at',
        'updated_at'
    ]
    collection_fields = model.model_fields

    filtering_fields = [
        'id',
        'sourceID',
        'name',
        'organization',
        'site',
        'manager',
        'created_at',
        'updated_at',
        'employeeID',
        'primary_email',
        'supportID',
        'roles'
    ]

    def __init__(self, url: str, token: str, account: str) -> None:
        super().__init__(
            url=url,
            token=token,
            account=account,
            endpoint='people',
        )

    def create(self, model: Person) -> Person:
        model = model.deserialize()
        return Person.serialize(**super().create(model))

    def list(
            self,
            fields: list[str] = None,
            predefined_filter: str | None = None,
            filters: list | None = None,
            sort: str | None = None
    ):
        return [Person.serialize(**p) for p in super().list(fields, predefined_filter, filters, sort)]

    def get(self, id_: int) -> Person:
        return Person.serialize(**super().get(id_))

    def update(self, model: Person) -> Person:
        deserialized = model.deserialize()
        return Person.serialize(**super().update(id_=model.id, data=deserialized))
