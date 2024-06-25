from .api import Api
from .models.organizations import Organization, OrganizationCreateModel


class OrganizationsApi(Api):
    AVAIABLE_PREDEFINED_FILTERS = [
        'disabled',
        'enabled',
        'external',
        'internal',
        'trusted',
        'directory',
        'support_domain',
        'managed_by_me'

    ]
    SORT_FIELDS = [
        'id', 'sourceID', 'name', 'created_at', 'updated_at'
    ]
    COLLECTION_FIELDS = [
        'id', 'sourceID', 'name', 'parent', 'manager', 'created_at', 'updated_at'
    ]

    FILTERING = [
        'id', 'source', 'sourceID', 'name', 'disabled', 'create_at', 'updated_at', 'disabled', 'financialID', 'parent'
    ]

    def __init__(self, url, token, account):
        super().__init__(url=url,
                         endpoint='organizations',
                         token=token,
                         account=account)

    def get(self, id_: int):
        json = super().get(id_).json()
        return Organization(**json)

    def create(self, organization: OrganizationCreateModel):
        json = super().post(organization.model_dump(exclude_unset=True)).json()
        return Organization(**json)

    def update(self, id_: int, organization: OrganizationCreateModel):
        json = super().patch(id_, organization.model_dump(exclude_unset=True)).json()
        return Organization(**json)

    def list(self, fields: list[str] = None,
             predefined_filter: str | None = None,
             filters: dict | None = None,
             sort: str | None = None):
        if predefined_filter and predefined_filter.lower() not in self.AVAIABLE_PREDEFINED_FILTERS:
            raise ValueError(f'Predefined filter {predefined_filter} is not available! Check documentation: '
                             f'https://developer.4me.com/v1/organizations/#list-organizations')
        if sort and sort.lower() not in self.SORT_FIELDS:
            raise ValueError(f'Sort field {sort} is not available! Check documentation: '
                             f'https://developer.4me.com/v1/organizations/#list-organizations')
        if filters and not all([field.lower() in self.FILTERING for field in filters.keys()]):
            raise ValueError(f'Filter fields {filters.keys()} are not available! Check documentation: '
                             f'https://developer.4me.com/v1/organizations/#list-organizations')
        if fields:
            if not all([field.lower() in self.COLLECTION_FIELDS for field in fields]):
                raise ValueError(f'Fields {fields} are not available! Check documentation: '
                                 f'https://developer.4me.com/v1/organizations/#list-organizations')
        if predefined_filter and filters:
            raise ValueError('You can use predefined_filter or filters, not both!')
        data = super().list(fields=fields,
                            predefined_filter=predefined_filter,
                            filters=filters,
                            sort=sort)
        return [Organization(**item) for item in data]
