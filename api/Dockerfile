# Security rationale: the base image is pinned exactly to keep builds
# reproducible and to make image vulnerability findings traceable.
FROM python:3.11.11-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

COPY requirements.txt .

# Security rationale: dependencies are installed from pinned requirements so
# supply-chain changes are explicit in code review and scanner results.
RUN python -m pip install --upgrade pip==24.3.1 \
    && python -m pip install --prefix=/install --no-cache-dir -r requirements.txt

# TODO: migrate the runtime stage to a distroless Python image once dependency
# and operational requirements are validated for that base.
# Security rationale: slim is used temporarily to keep the runtime small while
# preserving enough compatibility for Phase 0 diagnostics.
FROM python:3.11.11-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:${PATH}"

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app ./app

# Security rationale: running as a non-root user limits the blast radius if the
# application process is compromised.
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
