from collections import deque

with open("20/input.txt") as f:
    data = f.readlines()

modules = {}


class PulseQueue:
    def __init__(self):
        self.queue = deque()
        self.low_pulses = 0
        self.high_pulses = 0

    def queue_low(self, sender, receiver):
        self.queue.append(
            lambda: modules.get(receiver, Module(receiver, [])).low_pulse(sender)
        )
        self.low_pulses += 1

    def queue_high(self, sender, receiver):
        self.queue.append(
            lambda: modules.get(receiver, Module(receiver, [])).high_pulse(sender)
        )
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

    def add_input(self, name):
        self.inputs[name] = "low"

    def __pulse(self, sender, pulse):
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

for module in modules.values():
    if isinstance(module, ConjuctionModule):
        for m in modules.values():
            if module.name in m.receivers:
                module.add_input(m.name)

button = ButtonModule()

for _ in range(1000):
    button.low_pulse(None)
    while not queue.empty():
        queue.next_pulse()

print(queue.low_pulses * queue.high_pulses)
