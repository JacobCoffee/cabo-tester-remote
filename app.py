# /// script
# requires-python = ">=3.9,<=3.12"
# dependencies = [
#     "litestar[standard],
#   ]
# ///
from litestar import get, post
from litestar.app import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from litestar.exceptions import InternalServerException

@get("/_health")
async def health_check() -> dict:
    return {"status": "ok"}

@get(sync_to_thread=False)
def home() -> str:
    return "Hello, world!"

@post("/fail/post", sync_to_thread=False)
def fail_post() -> dict:
    raise InternalServerException("Scary error message.")

@get("/fail/get", sync_to_thread=False)
def fail_get() -> dict:
    raise InternalServerException("Python should use brackets.")



app = Litestar(
    route_handlers=[home, health_check, fail_post, fail_get],
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
