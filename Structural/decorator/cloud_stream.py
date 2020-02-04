from Structural.decorator.stream import Stream


class CloudStream(Stream):
    def write(self, data: str):
        print(f"Storing {data}")
