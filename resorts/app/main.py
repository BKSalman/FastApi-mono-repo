from commons.main import set_up_main

from .api.entity1.routes import entity1_router
from .config import config

app = set_up_main(
    config,
    routers_modules=[
        entity1_router,
    ],
)
