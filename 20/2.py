from collections import deque
import math

with open("20/input.txt") as f:
    data = f.readlines()

modules = {}


class PulseQueue:
    def __init__(self):
        self.queue = deque()
        self.low_pulses = 0
        self.high_pulses = 0

    def queue_low(self, sender, receiver):
        self.queue.append(lambda: modules.get(receiver).low_pulse(sender))
        self.low_pulses += 1

    def queue_high(self, sender, receiver):
        self.queue.append(lambda: modules.get(receiver).high_pulse(sender))
        self.high_pulses += 1

    def next_pulse(self):
        self.queue.popleft()()

    def empty(self):
        return len(self.queue) == 0


queue = PulseQueue()


class Module:
    def __init__(self, name: str, receivers: list[str]) -> None:
        self.name = name
        self.receivers = receivers

    def low_pulse(self, sender):
        pass

    def high_pulse(self, sender):
        pass

    def queue_low(self):
        for n in self.receivers:
            queue.queue_low(self, n)

    def queue_high(self):
        for n in self.receivers:
            queue.queue_high(self, n)


class FlipFlopModule(Module):
    def __init__(self, name: str, receivers) -> None:
        super().__init__(name, receivers)
        self.on = False

    def low_pulse(self, sender):
        if self.on:
            self.queue_low()
            self.on = False
        else:
            self.queue_high()
            self.on = True


class ConjuctionModule(Module):
    def __init__(self, name: str, receivers) -> None:
        super().__init__(name, receivers)
        self.inputs = {}
        self.high_length = {}
        self.pulse_counter = {}

    def add_input(self, name):
        self.inputs[name] = "low"
        self.high_length[name] = None

    def __pulse(self, sender, pulse):
        # collect how many button presses it takes to receive high pulse from input
        if not self.high_length[sender.name] and pulse == "high":
            self.high_length[sender.name] = button_presses

        self.inputs[sender.name] = pulse
        if all([p == "high" for p in self.inputs.values()]):
            self.queue_low()
        else:
            self.queue_high()

    def low_pulse(self, sender):
        self.__pulse(sender, "low")

    def high_pulse(self, sender):
        self.__pulse(sender, "high")


class BroadcasterModule(Module):
    def low_pulse(self, sender):
        self.queue_low()

    def high_pulse(self, sender):
        self.queue_low()


class ButtonModule(Module):
    def __init__(self):
        super().__init__("button", ["broadcaster"])

    def low_pulse(self, sender):
        self.queue_low()


class MachineOn(Exception):
    pass


class LCM(Exception):
    pass


class OutputModule(Module):
    def __init__(self):
        super().__init__("rx", [])
        self.lcm = None

    def low_pulse(self, sender):
        raise MachineOn()

    def high_pulse(self, sender):
        # if we have high pulse cycle lengths for all inputs of sender, compute lcm
        if all(sender.high_length.values()):
            self.lcm = math.lcm(*sender.high_length.values())
            raise LCM()


# load modules
for line in data:
    sender, receiver = line.strip().split(" -> ")
    if sender == "broadcaster":
        modules[sender] = BroadcasterModule(sender, receiver.split(", "))
    elif sender[0] == "%":
        modules[sender[1:]] = FlipFlopModule(sender[1:], receiver.split(", "))
    elif sender[0] == "&":
        modules[sender[1:]] = ConjuctionModule(sender[1:], receiver.split(", "))
    else:
        raise Exception("Unknown module type")

# pair conjuction modules with their inputs
for module in modules.values():
    if isinstance(module, ConjuctionModule):
        for m in modules.values():
            if module.name in m.receivers:
                module.add_input(m.name)

button = ButtonModule()
output = OutputModule()
modules[output.name] = output

button_presses = 0
try:
    while True:
        button.low_pulse(None)
        button_presses += 1
        while not queue.empty():
            queue.next_pulse()
except MachineOn:
    print(button_presses)
except LCM:
    print(output.lcm)
