class TinyAgent:
    def __init__(self):
        self.llm = None
        self.memory = None
        self.tools = None
        self.planner = None
    
    def run(self, task: str):
        """Run the agent on a task"""
        return self._step(task)

    def _step(self, task: str):
        """Run a single step of the agent on a task"""
        return f"Received: {task}"

    def _execute_action(self, action: str):
        """Execute a tool action"""
        return f"Executed: {action}"