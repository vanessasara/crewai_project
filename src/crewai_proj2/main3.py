from pydantic import BaseModel
from crewai.flow import Flow, start, listen
from crewai_proj2.crews.poem_crew.dev_crew import DevCrew


class DevState(BaseModel):
    problem: str = ""
    solution: str = ""
    reviewed_solution: str = ""

class DevFlow(Flow[DevState]):

    @start()
    def generate_problem(self):
        print("Generating a problem for the developers")
        self.state.problem = input("Write prompt for python code:")
        print("Problem selected:", self.state.problem)

    @listen(generate_problem)
    def generate_solution(self):
        print("Generating solution by Junior Developer")
        result = (
            DevCrew()
            .crew()
            .kickoff(inputs={"problem": self.state.problem})
        )
        print("Solution generated:", result.raw)
        self.state.solution = result.raw

    @listen(generate_solution)
    def review_solution(self):
        print("Reviewing solution by Senior Developer")
        result = (
            DevCrew()
            .crew()
            .kickoff(inputs={"problem": self.state.problem, "solution": self.state.solution})
        )
        print("Reviewed solution:", result.raw)
        self.state.reviewed_solution = result.raw

    @listen(review_solution)
    def save_solution(self):
        print("Saving reviewed solution")
        with open("reviewed_solution.md", "w") as f:
            f.write(self.state.reviewed_solution)


def kickoff():
    dev_flow = DevFlow()
    dev_flow.kickoff()


def plot():
    dev_flow = DevFlow()
    dev_flow.plot()


if __name__ == "__main__":
    kickoff()