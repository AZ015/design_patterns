from Behavioral.strategy.compressor import Compressor


class PngCompressor(Compressor):
    def compress(self) -> str:
        return "PNG compress"
