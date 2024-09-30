FROM python:3.10.15-slim-bookworm as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y \
  --no-install-recommends \
  gcc \
  wget && \
  GRPC_HEALTH_PROBE_VERSION=v0.4.34 && \
  wget -qO/bin/grpc_health_probe "https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64"

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
COPY --from=python-deps /bin/grpc_health_probe /bin/grpc_health_probe
ENV PATH="/.venv/bin:$PATH"

RUN chmod +x /bin/grpc_health_probe

# Create and switch to a new user
WORKDIR /app

# Install application into container
COPY api/ .

EXPOSE 8081

# Run the application
ENTRYPOINT ["python", "main.py"]