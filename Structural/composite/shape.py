from Structural.composite.component import Component


class Shape(Component):
    def render(self):
        print("Render Shape")

    def move(self):
        print("Move Shape")
