# from OLD_VERSION.api.models.people import PersonCreateModel
# from OLD_VERSION.py4me import Connection
# from OLD_VERSION.utils import PATAuth
#
from pprint import pprint

token = 'bziGcS9f20uIexBZ4qBgLN7o1HyPe4XT35LH0HV3wG1gSF1q6VneVU6rx6DEx5mOdbBRulBcdjRn3kNBGqPl5MbxrhCiUd4PUj4VfNLZD86jt1E2'

#
# result = conn.people.update(4216955, PersonCreateModel(name='PapitoFromSDK5', disabled=True))
# print(result.name, result.manager.name, result.disabled)
#
#
#
# # TODO: Dodać filtry do list, zdefiniowane są juz klasy, trzeba ogarnąć ich używanie, wygląda to DOBRZE.

#
# from src.py4me.auth.auth import PATAuth
# from src.py4me.py4me import Connection
#
# conn = Connection('qa', 'global', PATAuth(token, 'rossmann-it'))


from src.py4me.auth import PATAuth
from src.py4me.py4me import Connection

# print(p := Person.serialize(id=1, name='Papito', primary_email='test@test.py',
#                             organization=Organization.serialize(id=1, name='Rossmann IT')))
# print(p.name, p.primary_email)
# print(p.deserialize())
# print(p.to_json())

conn = Connection(
    region='global',
    environment='qa',
    auth=PATAuth(account='rossmann-it',
                 token=token),
)

# y = conn.people.list(predefined_filter='enabled', fields=['custom_fields'])
# y = conn.people.create(model=Person(
#     name='PapitoFromSDK1',
#     primary_email='papi@to5.pl',
#     disabled=True
# ))
z = conn.people.get(4297982)
print(z)
z.vip = False
y = conn.people.update(z)
pprint(y)
# for x in y:
#     if x.custom_fields:
#         pprint(x)
