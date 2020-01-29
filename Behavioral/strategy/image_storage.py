from Behavioral.strategy.compressor import Compressor
from Behavioral.strategy.filter import Filter
from Behavioral.strategy.high_contrast import HighContrast
from Behavioral.strategy.jpeg_compressor import JpegCompressor


class ImageStore:

    def __init__(self, compressor: Compressor, filtr: Filter) -> None:
        self._compressor = compressor
        self._filter = filtr

    def store(self, file_name) -> None:
        with open(file_name, "w") as file:
            file.write(self._compressor.compress())
            file.write("\n")
            file.write(self._filter.apply())


if __name__ == '__main__':
    jpeg_compr = JpegCompressor()
    high_contrast = HighContrast()

    storage = ImageStore(jpeg_compr, high_contrast)
    storage.store("test.txt")
