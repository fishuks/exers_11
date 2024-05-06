import turtle
import random

class Molecule(turtle.Turtle):
    def __init__(self, x, y, radius, color, speed):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(x, y)
        self.shapesize(radius / 10)
        self.color(color)
        self.speed = speed
        self.radius = radius

    def move(self):
        angle = random.uniform(0, 360)
        distance = random.uniform(0, self.speed)
        new_x = self.xcor() + distance * random.uniform(-1, 1)
        new_y = self.ycor() + distance * random.uniform(-1, 1)
        if abs(new_x) > 380 or abs(new_y) > 280:
            self.move()  
            return

        self.goto(new_x, new_y)

    def bounce(self, other_molecule):
        distance = self.distance(other_molecule)
        if distance <= (self.radius + other_molecule.radius) / 2:
            self.move()
            other_molecule.move()

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor('white')

    molecules = []
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        radius = random.uniform(10, 30)
        color = random.choice(['red', 'blue', 'green', 'yellow', 'purple'])
        speed = random.uniform(1, 5)
        molecule = Molecule(x, y, radius, color, speed)
        molecules.append(molecule)

    while True:
        for molecule in molecules:
            molecule.move()
            for other_molecule in molecules:
                if molecule != other_molecule:
                    molecule.bounce(other_molecule)

        screen.update()

if __name__ == '__main__':
    main()