from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


@CrewBase
class ResearchCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            tools=[search_tool],
        )

    @agent
    def draft_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["draft_agent"],
        )

    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config["research"],
        )

    @task
    def draft(self) -> Task:
        return Task(
            config=self.tasks_config["draft"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
