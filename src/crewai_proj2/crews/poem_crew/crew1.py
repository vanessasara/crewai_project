import os
from dotenv import load_dotenv
from crewai import Agent
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper

# Set up your SERPER_API_KEY key in an .env file, eg:
# SERPER_API_KEY=<your api key>
load_dotenv()

search = GoogleSerperAPIWrapper()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about markets, companies, and trends."
    search: GoogleSerperAPIWrapper = Field(default_factory=GoogleSerperAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"

# Create Agents
researcher = Agent(
    role='Research Analyst',
    goal='Gather current market data and trends',
    backstory="""You are an expert research analyst with years of experience in
    gathering market intelligence. You're known for your ability to find
    relevant and up-to-date market information and present it in a clear,
    actionable format.""",
    tools=[SearchTool()],
    verbose=True
)
