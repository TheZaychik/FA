from aiohttp import web
routes = web.RouteTableDef()

@routes.post('/hs/bank/send')
async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8080)
