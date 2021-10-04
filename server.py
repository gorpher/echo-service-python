from sanic import Sanic
from sanic.log import logger
from sanic.response import json

app = Sanic("echo-service")


@app.route('/', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
async def index(request):
    print('header', request.headers.items())
    body = request.body
    content_type = request.headers.get('content-type')
    json_value = None
    if content_type == 'application/json':
        json_value = request.json
    return json({
        'headers': list(request.headers.items()),
        'json': json_value,
        'args': request.args,
        'form': request.form,
        'method': request.method,
        'body': str(body, 'utf-8'),
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, access_log=True)
