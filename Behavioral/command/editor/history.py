from typing import Deque
from collections import deque

from Behavioral.command.editor.undoable_command import UndoableCommand


class History:
    def __init__(self):
        self._commands: Deque[UndoableCommand] = deque()

    def push(self, command: UndoableCommand) -> None:
        self._commands.append(command)

    def pop(self) -> UndoableCommand:
        return self._commands.pop()

    def size(self):
        return len(self._commands)