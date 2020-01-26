from Behavioral.strategy.compressor import Compressor


class JpegCompressor(Compressor):
    def compress(self) -> str:
        return  "JPEG compress"
