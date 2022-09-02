from commons.main import set_up_main

from .api.users.routes import users_router
from .config import config

app = set_up_main(
    config,
    routers_modules=[
        users_router,
    ],
)
