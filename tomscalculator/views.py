from aiohttp import web
import aiohttp_jinja2
import os

from tomscalculator.common import checkfields, process_calc


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'message': 'Lets calculate (pid %s)' % os.getpid()}


async def calculate(request):
    data = await request.post()
    amount = data.get('amount')
    price = data.get('price')
    statecode = data.get('statecode')

    if not checkfields(amount, price, statecode):
        return web.json_response({'status': 'error'})

    result = process_calc(amount, price, statecode)
    result['status'] = 'success'

    return web.json_response(result)
