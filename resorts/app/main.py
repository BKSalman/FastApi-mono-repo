from commons.main import set_up_main

from .api.resorts.routes import resorts_router
from .config import config

app = set_up_main(
    config,
    routers_modules=[
        resorts_router,
    ],
)
