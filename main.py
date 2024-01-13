from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request

from scraper import get_scrap_completion

flask_app = Flask(__name__)


@flask_app.post('/v1/chat/completions/')
async def get_completion():
    response = await get_scrap_completion(request.json['model'], request.json['messages'])
    if response is None:
        return {'error': 'no completion available'}
    return {
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response,
                }
            }
        ]
    }


app = WsgiToAsgi(flask_app)

#app.run(debug=True)
