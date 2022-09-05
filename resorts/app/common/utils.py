import requests
from fastapi import Depends
from resorts.app.api.resorts.schemas import UserRequest
from commons.schemas import UserToken
import logging

logger = logging.getLogger(__name__)


def login_user(user: UserRequest):
    res = requests.post("http://users-api/users/login", json=user.dict())
    res_json = res.json()
    return UserToken(
        access_token=res_json["access_token"],
        refresh_token=res_json["refresh_token"],
    )


def get_verified_current_user(token: UserToken = Depends(login_user)):
    headers = {"Authorization": "Bearer {}".format(token.access_token)}
    res = requests.get("http://users-api/users/me", headers=headers)
    return res.json()
