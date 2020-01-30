from Behavioral.command.editor.history import History
from Behavioral.command.elements import Command


class UndoCommand(Command):
    def __init__(self, history: History) -> None:
        self._history = history

    def execute(self):
        if self._history.size() > 0:
            self._history.pop().un_execute()
