from aiohttp import web

from . import views


def setup_routes(app):
    app.router.add_view('/', views.MainView)
