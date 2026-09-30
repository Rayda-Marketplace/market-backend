import logging

import grpc
import uvloop

from identity_service.bootstrap.settings.application import ApplicationSettings
from identity_service.bootstrap.settings.logging_ import LoggingSettings
from identity_service.bootstrap.setup import setup_logging

logger = logging.getLogger(__name__)


async def main() -> None:
    app_settings = ApplicationSettings.load()
    logging_settings = LoggingSettings.load()

    setup_logging(logging_settings)

    logger.info("creating gRPC server...")
    host = app_settings.host
    port = app_settings.port

    server = grpc.aio.server()
    server.add_insecure_port(f"{host}:{port}")
    logger.info("server created!")

    logger.info("starting gRPC server...")
    await server.start()
    logger.info(
        f"Service {app_settings.service_name} started with gRPC on {host}:{port}"
    )

    try:
        await server.wait_for_termination()
    finally:
        await server.stop(grace=5)


if __name__ == "__main__":
    uvloop.run(main())
