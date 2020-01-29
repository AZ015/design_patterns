from typing import List

from Behavioral.visitor.html_node import HtmlNode
from Behavioral.visitor.operation import Operation


class HtmlDocument:
    def __init__(self):
        self._nodes: List[HtmlNode] = []

    def add(self, html_node: HtmlNode):
        self._nodes.append(html_node)

    def execute(self, operation: Operation):
        [node.execute(operation) for node in self._nodes]
