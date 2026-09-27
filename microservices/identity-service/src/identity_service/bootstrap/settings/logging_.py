import enum

from pydantic_settings import SettingsConfigDict

from identity_service.bootstrap.settings.base import BasePydanticEnvSettings


class LoggingLevel(enum.StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LoggingSettings(BasePydanticEnvSettings):
    level: LoggingLevel = LoggingLevel.INFO
    fmt: str = (
        "[%(asctime)s.%(msecs)03d] [%(threadName)s] "
        "%(funcName)20s "
        "%(module)s:%(lineno)d "
        "%(levelname)-8s - %(message)s"
    )
    datefmt: str = "%Y-%m-%d %H:%M:%S"

    model_config = SettingsConfigDict(env_prefix="LOGGING_")
