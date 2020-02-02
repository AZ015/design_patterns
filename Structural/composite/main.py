from Structural.composite.group import Group
from Structural.composite.shape import Shape

if __name__ == '__main__':
    group_1 = Group()
    group_1.add(Shape())
    group_1.add(Shape())

    group_2 = Group()
    group_2.add(Shape())
    group_2.add(Shape())

    group = Group()
    group.add(group_1)
    group.add(group_2)

    group.render()
    group.move()
