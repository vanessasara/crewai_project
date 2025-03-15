from pydantic import BaseModel
from crewai.flow import Flow, start, listen
from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai.tools import BaseTool
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Define the Search Tool
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


# Define Research State
class ResearchState(BaseModel):
    query: str = ""
    search_results: str = ""


# Define Research Flow
class ResearchFlow(Flow[ResearchState]):

    @start()
    def get_query(self):
        print("Fetching search query from user...")
        self.state.query = input("Enter your market research query: ")
        print("Query received:", self.state.query)

    @listen(get_query)
    def perform_search(self):
        print("Performing search using GoogleSerper API...")
        
        search_tool = SearchTool()
        result = search_tool._run(self.state.query)

        print("Search results received:", result)
        self.state.search_results = result

    @listen(perform_search)
    def save_results(self):
        print("Saving search results...")
        with open("search_results.md", "w") as f:
            f.write(self.state.search_results)
        print("Results saved successfully.")


# Kickoff function
def kickoff():
    research_flow = ResearchFlow()
    research_flow.kickoff()


# Plot function (optional for debugging)
def plot():
    research_flow = ResearchFlow()
    research_flow.plot()


if __name__ == "__main__":
    kickoff()
