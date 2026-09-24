from fastapi import FastAPI

from backend.app.core.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
