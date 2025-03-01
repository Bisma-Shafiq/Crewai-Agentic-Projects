from crewai.flow.flow import Flow, listen, start
from litellm import completion

from research_dual_agent_02.crews.research_agent.research_agent import ResearchCrew


class ResearchFlow(Flow):

    @start()
    def run_research_crew(self):
        output = ResearchCrew().crew().kickoff(inputs={"topic": "Agentic AI"})
        return output.raw


def kickoff():
    research_flow = ResearchFlow()
    result = research_flow.kickoff()
    print(result)
