from typing import Self

from pydantic_settings import BaseSettings, SettingsConfigDict


class BasePydanticEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @classmethod
    def load(cls) -> Self:
        return cls()
