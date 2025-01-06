# /// script
# requires-python = ">=3.9,<=3.12"
# dependencies = [
#     "litestar[standard],
#   ]
# ///
from litestar import get, post
from litestar.app import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from litestar.exceptions import InternalServerException
from litestar.response import Template
from litestar.template import TemplateConfig


@get("/_health")
async def health_check() -> dict:
    return {"status": "ok"}


@get(sync_to_thread=False)
def home() -> Template:
    return Template(
        template_str="""
    <html>
    <head>
        <title>Litestar</title>
    </head>
    <body>
        <h1>Hello, Litestar!</h1>
        <a href="/api">API</a>
        <br>
        <a href="/fail/get">Fail GET</a>
        <br>
        <form action="/fail/post" method="post">
            <input type="submit" value="Fail POST" />
        </form>
    </body> 
    </html>
    """
    )


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
        path="/api",
    ),
    template_config=TemplateConfig(directory="templates", engine=JinjaTemplateEngine),
)

if __name__ == "__main__":
    from litestar.__main__ import run_cli

    run_cli()
