from Structural.decorator.stream import Stream


class Encrypted(Stream):
    def __init__(self, stream: Stream):
        self._stream = stream

    def write(self, data: str):
        encrypted = self._encrypt(data)
        self._stream.write(encrypted)

    def _encrypt(self, data: str) -> str:
        return "!@#$%^&*()_"
