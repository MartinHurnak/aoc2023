import copy
import numpy as np

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
            self.operator = "<" if "<" in condition else ">"
            self.category, val = condition.split(self.operator)
            self.value = int(val)

    def intersect(self, low, high):
        if self.operator == "<":
            if high < self.value:
                return None, (low, high)
            else:
                return (low, min(high, self.value - 1)), (
                    self.value,
                    high,
                ) if self.value < high else None
        elif self.operator == ">":
            if low > self.value:
                return None, (low, high)
            else:
                return (max(low, self.value + 1), high), (
                    low,
                    self.value,
                ) if low < self.value else None


class Workflow:
    def __init__(self, workflow_str: str):
        self.name, other = workflow_str.strip().strip("}").split("{")
        self.steps = [Step(s) for s in other.split(",")]

    def evaluate(self, intervals: dict, depth=0):
        possibilities = 0
        for step in self.steps:
            new_intervals = copy.deepcopy(intervals)
            if step.conditional:
                inner, outer = step.intersect(*intervals[step.category])
                if inner:
                    new_intervals[step.category] = inner
                    # print('  ' *depth, self.name, "->", step.next_workflow, new_intervals)
                    possibilities += workflows[step.next_workflow].evaluate(
                        new_intervals, depth + 1
                    )
                if not outer:
                    break
                else:
                    intervals[step.category] = outer
            else:
                # print('  ' *depth, self.name, "->", step.next_workflow, new_intervals)
                possibilities += workflows[step.next_workflow].evaluate(
                    new_intervals, depth + 1
                )
                break
        return possibilities


class AcceptWorkflow(Workflow):
    def __init__(self):
        self.name = "A"
        self.steps = []

    def evaluate(self, intervals: dict, depth=0):
        possibilities = np.prod(
            [high - low + 1 for low, high in intervals.values()], dtype=np.uint64
        )
        # print('  '*depth,"Accept", intervals, possibilities)
        return possibilities


class RejectWorkflow(Workflow):
    def __init__(self):
        self.name = "R"
        self.steps = []

    def evaluate(self, intervals: dict, depth=0):
        return 0


workflow_data, part_data = data.split("\n\n")


workflows = {}
for line in workflow_data.split("\n"):
    workflow = Workflow(line)
    workflows[workflow.name] = workflow

workflows["A"] = AcceptWorkflow()
workflows["R"] = RejectWorkflow()

intervals = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

print(workflows["in"].evaluate(intervals))
