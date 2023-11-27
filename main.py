from dotenv import load_dotenv

from util import inference
load_dotenv()
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from pathlib import Path

l2_prompt = inference("Level 3 prompt: Create a clock in HTML5/CSS/JavaScript.")
l1_prompt = inference(f"Level 2 prompt: {l2_prompt}")
result = inference(f"Level 1 prompt: {l1_prompt}")
Path('./.result.md').write_text(result)
print(result)