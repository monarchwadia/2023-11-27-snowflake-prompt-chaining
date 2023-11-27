from dotenv import load_dotenv
load_dotenv()

from util import RunManager

rm = RunManager()
l2_prompt = rm.inference("Level 3 prompt: Create a clock in HTML5/CSS/JavaScript.")
l1_prompt = rm.inference(f"Level 2 prompt: {l2_prompt}")
result = rm.inference(f"Level 1 prompt: {l1_prompt}")
print(result)
rm.save_result(result)