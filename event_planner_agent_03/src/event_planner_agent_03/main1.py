from crewai.flow.flow import Flow, listen, start
from litellm import completion

from event_planner_agent_03.crews.event_planner.event_planner import PlannerCrew

event_details = {
    "event_topic": "NVIDIA GTC AI Conference",
    "event_description": "A gathering of tech innovators "
    "and industry leaders "
    "to explore future technologies.",
    "event_city": "San Joes",
    "tentative_date": "2025-03-17",
    "expected_participants": 1000,
    "budget": 50000,
    "venue_type": "Conference Hall",
}


class PlannerFlow(Flow):

    @start()
    def run_planner_crew(self):
        output = PlannerCrew().crew().kickoff(inputs=event_details)
        return output.raw


def kickoff():
    planner_flow = PlannerFlow()
    result = planner_flow.kickoff()
    print(result)
