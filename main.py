from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request
from random import choice
import g4f
from flask_cors import CORS

flask_app = Flask(__name__)
cors = CORS(flask_app, resources={r"/v1/chat/completions/": {"origins": "*"}})

providers = {
    'gpt-3.5-turbo': [
        g4f.Provider.ChatBase,
        g4f.Provider.Bing,
        g4f.Provider.ChatgptAi,
        g4f.Provider.FakeGpt,
        g4f.Provider.FreeGpt,
        g4f.Provider.GPTalk,
        g4f.Provider.GptForLove,
        g4f.Provider.GptGo,
        g4f.Provider.Hashnode,
        g4f.Provider.You,
    ],
    'gpt-4': [
        g4f.Provider.Bing
    ]
}

allowed_models = [
    'gpt-3.5-turbo',
    'gpt-4'
]


async def get_scrap_completion(model: str, messages: list, tokens: int) -> str or None:
    if not model in allowed_models:
        return None

    try:
        response = await g4f.ChatCompletion.create_async(
            model=model,
            messages=messages,
            provider=choice(providers[model]),
            max_tokens=tokens,
        )
    except:
        response = await get_scrap_completion(model, messages, tokens)
        return response
    finally:
        return response


@flask_app.get('/')
async def ping():
    return "pong"


@flask_app.route('/v1/chat/completions/', methods=['GET', 'POST'], )
async def get_completion():
    if request.method == 'POST':
        response = await get_scrap_completion(request.json['model'], request.json['messages'], request.json['max_tokens'])
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
    return None


app = WsgiToAsgi(flask_app)

#app.run(debug=True)
