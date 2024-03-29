from random import choice
import g4f


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


async def get_scrap_completion(model: str, messages: list) -> str or None:
    if not model in allowed_models:
        return None


    response = await g4f.ChatCompletion.create_async(
        model=model,
        messages=messages,
        provider=choice(providers[model]),
    )
    return response
