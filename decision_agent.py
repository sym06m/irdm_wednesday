class DecisionAgent:
    def decide(self, question):
        if "agent" in question.lower():
            return "Decision: Use an AI agent"
        return "Decision: No agent required"

if __name__ == "__main__":
    agent = DecisionAgent()
    print(agent.decide("Should we use an agent for search?"))
