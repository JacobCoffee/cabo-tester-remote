# /// script
# requires-python = ">=3.9,<=3.12"
# dependencies = [
#     "litestar[standard],
#   ]
# ///

from litestar.app import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

app = Litestar(
    openapi_config=OpenAPIConfig(
        title="Litestar API",
        version="1.0.0",
        render_plugins=[
            ScalarRenderPlugin(),
        ],
    )
)

if __name__ == "__main__":
    from litestar.__main__ import run_cli

    run_cli()
