import aiohttp_jinja2
from aiohttp_jinja2 import render_template as render
import jinja2
from aiohttp import web


application = web.Application()
aiohttp_jinja2.setup(
    application,
    loader=jinja2.FileSystemLoader('templates')
)


async def index(request):
    name = request.match_info.get('name') or 'world'
    return web.json_response({
        'text': f'Hello {name}',
        'get_params': dict(request.query)
    })


async def post_example(request):
    data = await request.text()
    headers = request.headers
    return web.json_response({
        'message': 'ok',
        'data': data,
        'headers': dict(headers)
    })


class ClassView(web.View):
    async def get(self):
        return render(
            'index.html',
            self.request,
            context={
                'name': self.request.query.get('name') or 'world'
            }
        )

    async def post(self):
        return web.json_response({
            'method': 'POST'
        }, status=201)

    async def delete(self):
        return web.json_response({}, status=204)


application.add_routes([
    web.route('GET', '/hello/{name}', index, name='index'),
    web.post('/post', post_example, name='post'),
    web.route('*', '/class-example', ClassView, name='cbv_example')
])

web.run_app(application)
