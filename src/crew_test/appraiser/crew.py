from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore

@CrewBase
class AppraiserCrew():
    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'

    @agent
    def appraiser(self) -> Agent:
        return Agent(
            config=self.agents_config['appraiser'],
            verbose=True
        )

    @task
    def appraiser_task(self) -> Task:
        return Task(
            config=self.tasks_config['appraiser_task'],
            output_file='log/appraiser.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            language="pt-br"
        )
