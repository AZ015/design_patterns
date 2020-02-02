from typing import List

from Structural.composite.component import Component


class Group(Component):
    def __init__(self):
        self._components: List[Component] = []

    def add(self, component: Component) -> None:
        self._components.append(component)

    def render(self) -> None:
        [shape.render() for shape in self._components]

    def move(self):
        [shape.move() for shape in self._components]
