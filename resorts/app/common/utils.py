import requests
from fastapi import Depends

from resorts.app.api.resorts.schemas import UserRequest
from commons.schemas import UserToken


def login_user(token: UserRequest):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get("http://localhost:3001/users/me", headers=headers)
    return res


def get_verified_current_user(token: UserToken = Depends(login_user)):
    headers = {"Authorization": f"Bearer {token.access_token}"}
    res = requests.get("http://localhost:3001/users/me", headers=headers)
    return res
