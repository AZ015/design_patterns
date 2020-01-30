from abc import ABC, abstractmethod

from Behavioral.command.elements import Command


class UndoableCommand(Command):
    @abstractmethod
    def un_execute(self):
        pass

    def execute(self):
        pass
