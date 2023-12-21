with open("19/input.txt") as f:
    data = f.read()


class Step:
    def __init__(self, step_str: str):
        self.conditional = False
        self.operator = None
        self.next_workflow = None
        if "<" in step_str or ">" in step_str:
            self.conditional = True
        else:
            self.next_workflow = step_str

        if self.conditional:
            condition, self.next_workflow = step_str.split(":")
            if "<" in condition:
                self.__evaluate = self.__evaluate_less_than
                self.category, val = condition.split("<")
                self.value = int(val)
            elif ">" in condition:
                self.__evaluate = self.__evaluate_greater_than
                self.category, val = condition.split(">")
                self.value = int(val)

    def evaluate(self, part: dict):
        if not self.conditional:
            return True
        else:
            return self.__evaluate(part)

    def __evaluate_less_than(self, part: dict):
        return part[self.category] < self.value

    def __evaluate_greater_than(self, part: dict):
        return part[self.category] > self.value


class Workflow:
    def __init__(self, workflow_str: str):
        self.name, other = workflow_str.strip().strip("}").split("{")
        self.steps = [Step(s) for s in other.split(",")]

    def evaluate(self, part: dict):
        for step in self.steps:
            if step.evaluate(part):
                return step.next_workflow


workflow_data, part_data = data.split("\n\n")


workflows = {}
for line in workflow_data.split("\n"):
    workflow = Workflow(line)
    workflows[workflow.name] = workflow

result = 0
for line in part_data.split("\n"):
    part = {}
    for attr in line.strip("{}").split(","):
        k, v = attr.split("=")
        part[k] = int(v)

    workflow = workflows["in"]
    workflow_result = workflow.evaluate(part)
    while workflow_result not in ["R", "A"]:
        workflow = workflows[workflow_result]
        workflow_result = workflow.evaluate(part)

    if workflow_result == "A":
        result += sum(part.values())

print(result)
