from Behavioral.command.editor.history import History
from Behavioral.command.editor.html_document import HtmlDocument
from Behavioral.command.editor.undoable_command import UndoableCommand


class BoldCommand(UndoableCommand):
    def __init__(self, document: HtmlDocument, history: History):
        self._document = document
        self._history = history
        self._previous_content: str = ""

    def un_execute(self):
        self._document.content = self._previous_content

    def execute(self):
        self._previous_content = self._document.content
        self._document.make_bold()
        self._history.push(self)
