from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
import os 


# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL = os.environ.get("MODEL")


# Create a CSV knowledge source
csv_source = CSVKnowledgeSource(
    file_paths=["walmart.csv"]
)

gemini_llm = LLM(
    model=MODEL,
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About data",
    goal="You know everything about the data.",
    backstory="""You are a master at understanding data and  do their analysis.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    knowledge_sources=[csv_source],
    embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": GEMINI_API_KEY,
                },
            },
)
task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[csv_source], # Enable knowledge by adding the sources here. You can also add more sources to the sources list.
    embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": GEMINI_API_KEY,
                },
            },
)


def knowledge_csv():

    result = crew.kickoff(inputs={"question": "Give me a short analysis of this data set?"})
    print(result)