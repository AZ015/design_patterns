from Behavioral.command.elements.command import Command


class Button:
    def __init__(self, command: Command):
        self._command = command

    def click(self):
        self._command.execute()
