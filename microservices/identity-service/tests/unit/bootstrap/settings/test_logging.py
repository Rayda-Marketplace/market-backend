import pytest

from identity_service.bootstrap.settings.logging_ import LoggingLevel, LoggingSettings


@pytest.mark.parametrize(
    "logging_level",
    [
        LoggingLevel.DEBUG,
        LoggingLevel.INFO,
        LoggingLevel.WARNING,
        LoggingLevel.ERROR,
        LoggingLevel.CRITICAL,
    ],
)
def test_load_logging_settings_reads_env_vars(
    monkeypatch: pytest.MonkeyPatch,
    logging_level: LoggingLevel,
) -> None:
    monkeypatch.setenv("LOGGING_LEVEL", logging_level)
    monkeypatch.setenv("LOGGING_FMT", "%(levelname)s: %(message)s")
    monkeypatch.setenv("LOGGING_DATEFMT", "%H:%M:%S")

    sut = LoggingSettings.load()

    assert sut.level == logging_level
    assert sut.fmt == "%(levelname)s: %(message)s"
    assert sut.datefmt == "%H:%M:%S"
