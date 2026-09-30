#!/bin/bash

case "$1" in
  start)
    exec uv run --no-sync python -m src.identity_service.bootstrap
    ;;
  *)
    exec "$@"
    ;;
esac