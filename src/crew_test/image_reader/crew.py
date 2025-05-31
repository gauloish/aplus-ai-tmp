from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ..tools.vision_tool import VisionTool
from langchain_openai import ChatOpenAI
import requests
import base64

@CrewBase
class ImageReaderCrew():
    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'
    vision_tool = VisionTool()
    llm = ChatOpenAI(
        temperature=0.3,
        model_name="gpt-4o-mini",
    )
    
    @agent
    def image_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['image_reader'],
            tools=[self.vision_tool],
            verbose=True,
            llm=self.llm
        )

    @task
    def image_reader_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_reader_task'],
            output_file='log/image_reader.md'
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