from .base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def run(self, analysis):
        return {"report_text": "Generated report placeholder"}
