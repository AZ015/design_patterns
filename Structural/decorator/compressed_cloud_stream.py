from Structural.decorator.stream import Stream


class CompressedCloudStream(Stream):
    def __init__(self, stream: Stream):
        self._stream = stream

    def write(self, data: str):
        compressed = self._compressed(data)
        self._stream.write(compressed)

    def _compressed(self, data: str) -> str:
        return data[0:5]
