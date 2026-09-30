import pytest

from identity_service.bootstrap.settings.application import ApplicationSettings


def test_load_application_settings_reads_env_vars(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_SERVICE_NAME", "test-service")
    monkeypatch.setenv("APP_DEBUG", "1")
    monkeypatch.setenv("APP_HOST", "test-host")
    monkeypatch.setenv("APP_PORT", "12345")

    sut = ApplicationSettings.load()

    assert sut.service_name == "test-service"
    assert sut.debug is True
    assert sut.host == "test-host"
    assert sut.port == 12345
