# first-copilot

Create my first Azure AI Copilot

Setup:

1. Create an GPT-4o Deployment with Azure AI Studio \
   Copy the endpoint and depolyment name
2. Start WSL Ubuntu 22.04 with python 3.10

```
# Create .env with the Azure AI attributes from step 1.
cat << EOF > .env
AZURE_OPENAI_ENDPOINT="YOUR_AZURE_AI_SERVICE_ENDPOINT_URL"
CHAT_COMPLETIONS_DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
EOF

# Start an isoated python environment
python -m venv .venv
source .venv/bin/activate

# If needed, install
pip install openai
pip install azure.identity
pip install load_dotenv
```

3. Run the example

```
python app.py
```

4. Observe response like...

```
{
  "id": "chatcmpl-9TtLocVNTaMUY7Dlb5sGqUcn9tj4s",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "I'm not sure which specific service you are referring to, but generally speaking, many companies have specialized roles or teams responsible for opinion mining services, which can involve sentiment analysis and natural language processing to gauge public opinion from text data. In different organizations, the DRI (Directly Responsible Individual) might be:\n\n1. **Product Manager** - Oversees the development and direction of the opinion mining service.\n2. **Data Scientist/Analyst** - Directly responsible for the implementation and accuracy of the opinion mining algorithms.\n3. **Project Manager** - Manages the overall timeline and deliverables associated with the service.\n\nIf you have a specific company or service in mind, the DRI could be a named individual within that organization. Without more information, it's typically people within these roles who would be responsible for such a service.",
        "role": "assistant"
      },
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      }
    }
  ],
  "created": 1716911308,
  "model": "gpt-4o-2024-05-13",
  "object": "chat.completion",
  "system_fingerprint": "fp_5f4bad809a",
  "usage": {
    "completion_tokens": 166,
    "prompt_tokens": 42,
    "total_tokens": 208
  },
  "prompt_filter_results": [
    {
      "prompt_index": 0,
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      }
    }
  ]
}
```
