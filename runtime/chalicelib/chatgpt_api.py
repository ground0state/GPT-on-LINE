import os

import openai

# Model name
GPT3_MODEL = 'gpt-3.5-turbo'

# Maximum number of tokens to generate
MAX_TOKENS = 1024

# Create a new dict list of a system
SYSTEM_PROMPTS = [{
    'role': 'system',
    'content': '敬語を使うのをやめてください。友達のようにタメ口で話してください。また、絵文字をたくさん使って話してください。'
}]
# SYSTEM_PROMPTS = [{
#     'role': 'system',
#     'content': 'Please stop using polite language. Talk to me in a friendly way like a friend. Also, use a lot of emojis when you talk.'
# }]


def complete_chat(prompts):
    messages = SYSTEM_PROMPTS + prompts

    openai.api_key = os.environ['OPENAI_API_KEY']
    try:
        response = openai.ChatCompletion.create(
            model=GPT3_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS
        )
    except Exception as e:
        raise e
    response_text = response['choices'][0]['message']['content']
    created_at = int(response['created'])*1000
    return {
        'text': response_text,
        'created_at': created_at
    }
