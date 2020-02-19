#!/bin/env python3

import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from tomscalculator.routes import setup_routes

async def init_app():
    app = web.Application()
    setup_routes(app)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader('/'.join([str(pathlib.Path(__file__).parent), 'templates']))
    )
    return app


def main():
    app = init_app()
    web.run_app(app, port=8010)


if __name__ == '__main__':
    main()
