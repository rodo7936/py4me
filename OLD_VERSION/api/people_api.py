from .api import Api
from .models.people import Person,PersonCreateModel


class PeopleApi(Api):
    AVAIABLE_PREDEFINED_FILTERS = [
        'disabled',
        'enabled',
        'internal',
        'trusted',
        'directory',
        'support_domain',

    ]
    SORT_FIELDS = [
        'id', 'sourceID', 'name', 'created_at', 'updated_at', 'organization', 'site', 'manager'
    ]
    COLLECTION_FIELDS = [
        'id', 'sourceID', 'name', 'organization', 'site', 'manager', 'created_at', 'updated_at'
    ]

    FILTERING = [
        'id', 'source', 'sourceID', 'name', 'disabled', 'organization', 'site',
        'manager', 'created_at', 'updated_at', 'employeeID', 'primary_email', 'supportID', 'roles'
    ]

    def __init__(self, url, token, account):
        super().__init__(url=url,
                         endpoint='people',
                         token=token,
                         account=account)

    def get(self, id_: int):
        json = super().get(id_).json()
        return Person(**json)

    def create(self, person: Person):
        json = super().post(person.model_dump(exclude_unset=True)).json()
        return Person(**json)

    def update(self, id_: int, person: PersonCreateModel):
        json = super().patch(id_, person.model_dump(exclude_unset=True)).json()
        return Person(**json)

    def list(self, fields: list[str] = None,
             predefined_filter: str | None = None,
             filters: dict | None = None,
             sort: str | None = None):

        data = super().list(fields=fields,
                            predefined_filter=predefined_filter,
                            filters=filters,
                            sort=sort)
        return [Person(**item) for item in data]
