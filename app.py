# /// script
# requires-python = ">=3.9,<=3.12"
# dependencies = [
#     "litestar[standard],
#   ]
# ///
from litestar import get
from litestar.app import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

@get("/_health")
def health_check() -> dict:
    return {"status": "ok"}

@get()
def home() -> str:
    return "Hello, world!"

app = Litestar(
    route_handlers=[home, health_check],
    openapi_config=OpenAPIConfig(
        title="Litestar API",
        version="1.0.0",
        render_plugins=[
            ScalarRenderPlugin(),
        ],
        path="/api"
    )
)

if __name__ == "__main__":
    from litestar.__main__ import run_cli

    run_cli()
