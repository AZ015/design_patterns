from typing import Union

from Behavioral.visitor.anchor_node import AnchorNode
from Behavioral.visitor.heading_node import HeadingNode
from Behavioral.visitor.operation import Operation


class HighLightOperation(Operation):
    def apply(self, node: Union[AnchorNode, HeadingNode]):
        if isinstance(node, AnchorNode):
            print("Highlight-anchor")
        elif isinstance(node, HeadingNode):
            print("Highlight-heading")
