class PipelineAgent:
    def run(self, input_text):
        step1 = input_text.lower()
        step2 = step1.replace("ai", "artificial intelligence")
        return step2

if __name__ == "__main__":
    agent = PipelineAgent()
    print(agent.run("AI agents are powerful"))
