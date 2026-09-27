ARG python_version=3.14

FROM ghcr.io/astral-sh/uv:python${python_version}-trixie-slim

ARG environment="prod"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_HTTP_TIMEOUT=300
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /identity-service

COPY pyproject.toml uv.lock README.md ./

RUN if [ "${environment}" = "prod" ]; then \
        uv sync --frozen --no-cache --no-dev --no-install-project; \
    else \
        uv sync --frozen --no-cache --dev --no-install-project; \
    fi

COPY . .

RUN if [ "${environment}" = "prod" ]; then \
        uv sync --frozen --no-cache --no-dev; \
    else \
        uv sync --frozen --no-cache --dev; \
    fi

RUN groupadd -r runner
RUN useradd -r -g runner -m -s /usr/sbin/nologin runner
RUN chown -R runner:root /identity-service
RUN chmod -R g=u /identity-service

USER runner

EXPOSE 50051

ENTRYPOINT [ "sh", "/identity-service/docker-entrypoint.sh" ]