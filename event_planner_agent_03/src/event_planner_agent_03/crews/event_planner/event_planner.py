from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class PlannerCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def Venue_Coordinator_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config["Venue_Coordinator_Agent"],
        )

    @agent
    def logistics_manager_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config["logistics_manager_Agent"],
        )

    @agent
    def marketing_communications_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config["marketing_communications_Agent"],
        )

    @task
    def venue_task(self) -> Task:
        return Task(
            config=self.tasks_config["venue_task"],
        )

    @task
    def logistics_task(self) -> Task:
        return Task(
            config=self.tasks_config["logistics_task"],
        )

    @task
    def marketing_task(self) -> Task:
        return Task(
            config=self.tasks_config["marketing_task"],
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
