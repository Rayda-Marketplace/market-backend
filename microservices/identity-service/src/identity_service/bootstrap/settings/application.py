from pydantic_settings import SettingsConfigDict

from identity_service.bootstrap.settings.base import BasePydanticEnvSettings


class ApplicationSettings(BasePydanticEnvSettings):
    debug: bool = False
    service_name: str = "identity-service"
    host: str = "127.0.0.1"
    port: int = 50051

    model_config = SettingsConfigDict(env_prefix="APP_")
