from litellm import Router
import os

model_list = [{  # list of model deployments
    "model_name": "gpt-3.5-turbo",  # model alias
    "litellm_params": {  # params for litellm completion/embedding call
        "model": "azure/chatgpt-v-2",  # actual model name
        "api_key": os.getenv("AZURE_API_KEY"),
        "api_version": os.getenv("AZURE_API_VERSION"),
        "api_base": os.getenv("AZURE_API_BASE")
    }
}, {
    "model_name": "gpt-3.5-turbo",
    "litellm_params": {  # params for litellm completion/embedding call
        "model": "azure/chatgpt-functioncalling",
        "api_key": os.getenv("AZURE_API_KEY"),
        "api_version": os.getenv("AZURE_API_VERSION"),
        "api_base": os.getenv("AZURE_API_BASE")
    }
}, {
    "model_name": "gpt-3.5-turbo",
    "litellm_params": {  # params for litellm completion/embedding call
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
}]

router = Router(model_list=model_list)