import logging

from identity_service.bootstrap.settings.logging_ import LoggingSettings

logger = logging.getLogger(__name__)


def setup_logging(logging_settings: LoggingSettings) -> None:
    logging.basicConfig(
        level=logging_settings.level,
        datefmt=logging_settings.datefmt,
        format=logging_settings.fmt,
        force=True,
    )
    logger.info("Logging is set up!")
