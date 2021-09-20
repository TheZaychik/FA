from aiohttp import web
routes = web.RouteTableDef()

@routes.post('/hs/bank/send')
async def main(request):
    data = await request.post()
    print(data)
    return web.Response(text=f"Hi, {data['name']}")

@routes.get('/hello')
async def hello(request):
        return web.Response(text=f"Здарова!")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8080)
