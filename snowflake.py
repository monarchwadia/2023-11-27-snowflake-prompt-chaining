from dataclasses import dataclass

@dataclass
class ProcHistoryItem:
    """
    This class is used to store the context of the processor.
    """
    prompt: str
    context: object

type ProcHistory = list[ProcHistoryItem]

class Proc:
    def __call__(self, prompt: str, history: ProcHistory = []) -> ProcHistory:
        """
        This function is used to process the prompt and the user input.
        """
        raise NotImplementedError

class AddDotProc(Proc):
    """
    This class adds a dot to the end of the previous output.
    """
    def __call__(self, prompt: str, history: ProcHistory = []) -> ProcHistoryItem:
        return {
            "prompt": prompt,
            "result": prompt + '.'
        }

class Snowflake:
    """
    This class uses function chaining builder pattern to create a chain of prompts.
    The prompts are then used to prompt the LLM.
    """
    def __init__(self):
        self._chain: list[str] = []
        self._proc_history: ProcHistory = []
        self._proc: Proc = None
    
    def proc(self, proc: Proc):
        self._proc = proc
        return self

    def chain(self, prompt_file: str):
        """
        This function saves the prompt in the chain.
        """
        with open(prompt_file, "r") as f:
            prompt = f.read()
            self._chain.append(prompt)
        return self

    def prompt(self, user_input):
        """
        This function prompts the LLM with the chain of prompts. The prompts are fed to the next prompt in the chain.
        """

        next_prompt = user_input
        for chainstep in self._chain:
            new_item = self._proc(next_prompt, self._proc_history)
            next_prompt = new_item["result"]
            self._proc_history.append(new_item)
        return self
