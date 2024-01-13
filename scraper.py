from random import choice
import g4f

providers = [
    g4f.Provider.Bing,
    #g4f.Provider.GeekGpt,
    g4f.Provider.GptChatly,
    g4f.Provider.Liaobots,
]

allowed_models = [
    'gpt-3.5-turbo',
    ''
]


async def get_scrap_completion(model: str, messages: list) -> str or None:

    response = await g4f.ChatCompletion.create_async(
        model=model,
        messages=messages,
        provider=choice(providers),
    )
    return response
