from commons.config import (
    CommonBaseConfig,
    CommonProductionConfig,
    CommonStagingConfig,
    CommonTestingConfig,
    current_config,
)


class BaseConfig(CommonBaseConfig):
    APP_NAME: str = "users"
    ALGORITHM: str
    AUTH_JWT_KEY: str
    AUTH_TOKEN_EXPIRE_IN: int
    AUTH_SALT: str


class ProductionConfig(CommonProductionConfig, BaseConfig):  # type: ignore
    pass


class StagingConfig(CommonStagingConfig, BaseConfig):  # type: ignore
    pass


class TestingConfig(CommonTestingConfig, BaseConfig):  # type: ignore
    pass


config: BaseConfig = current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig)
