import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

# https://docs.python.org/3/library/venv.html
load_dotenv()
      
# https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#authenticate-with-defaultazurecredential
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
      
# https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/ai-services/openai/includes/python.md      
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
    api_version="2024-02-01",
)
      
completion = client.chat.completions.create(
    model=os.environ["CHAT_COMPLETIONS_DEPLOYMENT_NAME"],
    messages=[
        {
            "role": "user",
            "content": "Who is DRI?",
        },
        {
            "role": "assistant",
            "content": "DRI stands for Directly Responsible Individual of a service. Which service are you asking about?"
        },
        {
            "role": "user",
            "content": "Opinion mining service"
        }
    ]
)
      
print(completion.to_json())