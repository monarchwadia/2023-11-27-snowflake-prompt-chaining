from dotenv import load_dotenv
load_dotenv()

from run_manager import RunManager

rm = RunManager()
# l2_prompt = rm.l4_inference("Level 3 prompt: Create a clock in HTML5/CSS/JavaScript.")
# l1_prompt = rm.l4_inference(f"Level 2 prompt: {l2_prompt}")
# result = rm.l4_inference(f"Level 1 prompt: {l1_prompt}")
result = rm.simple_inference("Create a clock in HTML5/CSS/JavaScript")
result = rm.code_cleanup_inference(result)
rm.save_result(result)