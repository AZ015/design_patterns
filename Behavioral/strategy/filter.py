from abc import ABC, abstractmethod

from Structural.adapter.image import Image


class Filter(ABC):
    @abstractmethod
    def apply(self, image: Image) -> str:
        pass
