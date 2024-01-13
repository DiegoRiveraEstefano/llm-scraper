from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel

from scraper import get_scrap_completion


app = FastAPI(debug=True)


class Petition(BaseModel):
    model: str
    messages: list | None = None


@app.post('/v1/chat/completions/')
async def get_completion(petition: Petition):
    response = await get_scrap_completion(petition.model, petition.messages)
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