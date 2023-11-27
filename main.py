from dotenv import load_dotenv
load_dotenv()

from run_manager import RunManager

prompt = input("Level 1 prompt: ")

rm = RunManager()
# result = rm.simple_inference("Create a clock in HTML5/CSS/JavaScript")
l2_prompt = rm.l4_inference(f"Level 1 prompt: {prompt}")
l3_prompt = rm.l4_inference(f"Level 2 prompt: {l2_prompt}")
l4_prompt = rm.l4_inference(f"Level 3 prompt: {l3_prompt}")
raw_result = rm.l4_inference(f"Level 4 prompt: {l4_prompt}")
result = rm.code_cleanup_inference(raw_result)
rm.save_result(result)