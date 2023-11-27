from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from pathlib import Path
import os
import logging

# Constants & configurations
L4_PROMPT = Path('./prompt.md').read_text()
logging.basicConfig(filename='.log', encoding='utf-8', level=logging.INFO)

# Variables
messages: list[ChatCompletionMessage] = []

# Functions
def inference(prompt: str) -> ChatCompletionMessage:
    logging.info(f"inference ran with prompt:\n====================\n{prompt}\n====================")
    global messages
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages + [
            {"role": "system", "content": L4_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    returned_message = completion.choices[0].message
    messages = messages + [returned_message]
    content = returned_message.content
    logging.info(f"API returned with content:\n====================\n{content}\n====================")
    return content
    
