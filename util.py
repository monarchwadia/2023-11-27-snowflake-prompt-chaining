from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from pathlib import Path
import os
import logging
from datetime import datetime

# Constants & configurations
L4_PROMPT = Path('./prompt.md').read_text()
logging.basicConfig(filename='.log', encoding='utf-8', level=logging.INFO)

# Variables
messages: list[ChatCompletionMessage] = []

class RunManager:
    """
    A class that manages the running of the program.
    It outputs logs and results to files which match the current time.
    Logs are logged in `.output/YYYY-MM-DD-HH-MM-SS/.log`
    Results are saved in `.output/YYYY-MM-DD-HH-MM-SS/.result.md`
    """

    def __init__(self):
        # get current time in YYYY-MM-DD-HH-MM-SS format
        self.time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.logger = logging.getLogger(self.time)
        # ensure the output directory exists
        Path(f'.output/{self.time}').mkdir(parents=True, exist_ok=True)

        # configure logger to output to file
        handler = logging.FileHandler(f'.output/{self.time}/.log')
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        # configure result to output to file
        self.result_path = Path(f'.output/{self.time}/.result.md')
        
    def inference(self, prompt: str) -> ChatCompletionMessage:
        self.logger.info(f"inference ran with prompt:\n====================\n{prompt}\n====================")
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
        self.logger.info(f"API returned with content:\n====================\n{content}\n====================")
        return content
    
    def save_result(self, result: str):
        self.result_path.write_text(result)
        self.logger.info(f"Result saved to {self.result_path}")

# Functions

