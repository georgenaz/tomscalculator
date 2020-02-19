from tomscalculator.views import index, calculate

def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_post('/calc', calculate, name='calculate')
