from trajectory import Trajectory
from LLM import LLM

class TinyAgent:
    """A minimal, modular, and educational agent framework"""
    def __init__(self):
        self.llm = LLM(model="gemma4:e4b")
        self.memory = None
        self.tools = None
        self.planner = None
        
        self.trajectory = Trajectory()
    
    def run(self, task: str):
        """Run the agent on a task"""
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str):
        """Run a single step of the agent on a task"""
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages=messages)
        self.trajectory.add(response=response)
        return response.content

    def _execute_action(self, action: str):
        """Execute a tool action"""
        return f"Executed: {action}"