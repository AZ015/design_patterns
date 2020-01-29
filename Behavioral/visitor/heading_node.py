from Behavioral.visitor.html_node import HtmlNode
from Behavioral.visitor.operation import Operation


class HeadingNode(HtmlNode):
    def execute(self, operation: Operation):
        operation.apply(self)
