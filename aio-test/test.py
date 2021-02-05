from aiohttp import web
import json


app = web.Application()
routes = web.RouteTableDef()


@routes.get('/')
async def regtools(request):
    return web.json_response('hello')


app.add_routes(routes)
if __name__ == '__main__':
    web.run_app(app)
