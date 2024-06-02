import json

from cache import rds
from structs import AuthDataModel


def get_auth_data(username: str):
    user = rds.get(username)
    if user:
        return AuthDataModel(**json.loads(user))
