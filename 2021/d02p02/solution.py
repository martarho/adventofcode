from dataclasses import dataclass

def load_commands():
    for line in open('../data/day02_input.txt', 'r'):
        command, value = line.rstrip().split(" ")
        yield (command, int(value)) 

@dataclass
class Coordinates:
    z: int
    x: int
    aim: int

    def forward(self, i):
        self.x += i
        self.z += self.aim * i
    def up(self, i):
        self.aim -= i
    def down(self, i):
        self.aim += i


position = Coordinates(0,0,0)
commands2func = {"up": position.up,
                "down": position.down,
                "forward": position.forward}
for command, value in load_commands():
    commands2func[command](value)

print(position)
print(position.z * position.x)