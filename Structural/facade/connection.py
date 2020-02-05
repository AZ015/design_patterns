class Connection:
    def __init__(self, ip_address: str):
        self._ip_address = ip_address

    def disconnect(self):
        print(f"Connection was disconnect from IP: {self._ip_address}")
