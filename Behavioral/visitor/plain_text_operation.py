from typing import Union

from Behavioral.visitor.anchor_node import AnchorNode
from Behavioral.visitor.heading_node import HeadingNode
from Behavioral.visitor.operation import Operation


class PlainTextOperation(Operation):

    def apply(self, node: Union[HeadingNode, AnchorNode]):
        if isinstance(node, AnchorNode):
            print("text-anchor")
        elif isinstance(node, HeadingNode):
            print("text-heading")
