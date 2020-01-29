from Behavioral.visitor.anchor_node import AnchorNode
from Behavioral.visitor.heading_node import HeadingNode
from Behavioral.visitor.highlight_operation import HighLightOperation
from Behavioral.visitor.html_document import HtmlDocument
from Behavioral.visitor.plain_text_operation import PlainTextOperation

if __name__ == '__main__':
    document = HtmlDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    document.execute(HighLightOperation())
    document.execute(PlainTextOperation())
