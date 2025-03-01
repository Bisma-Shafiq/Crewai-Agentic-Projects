from crewai.flow.flow import Flow, listen, start
from litellm import completion

from multiple_agents_02.crews.dev_crew.dev_crew import DevCrew


class DevFlow(Flow):

    @start()
    def run_dev_crew(self):
        output = (
            DevCrew()
            .crew()
            .kickoff(inputs={"problem": "write python code for classification problem"})
        )
        return output.raw


def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)
