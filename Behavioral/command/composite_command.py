from Behavioral.command.elements import Command


class CompositeCommand(Command):

    def __init__(self):
        self._commands = []

    def add(self, command: Command):
        self._commands.append(command)

    def execute(self):
        [command.execute() for command in self._commands]
