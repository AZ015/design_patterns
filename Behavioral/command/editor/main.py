from Behavioral.command.editor.bold_command import BoldCommand
from Behavioral.command.editor.history import History
from Behavioral.command.editor.html_document import HtmlDocument
from Behavioral.command.editor.undo_command import UndoCommand

if __name__ == '__main__':
    history = History()
    document = HtmlDocument()
    document.content = "Hello world"

    bold_command = BoldCommand(document, history)
    bold_command.execute()
    print(document.content)

    bold_command.un_execute()
    print(document.content)

    undo_command = UndoCommand(history)
    undo_command.execute()
    print(document.content)

