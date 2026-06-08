from .base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def run(self, query: str):
        return {"news": [], "query": query}
