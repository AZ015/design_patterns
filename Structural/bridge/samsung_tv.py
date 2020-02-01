from Structural.bridge.device import Device


class SamsungTV(Device):
    def turn_on(self):
        print("Samsung turn on")

    def turn_off(self):
        print("Samsung turn off")

    def set_channel(self, number: int):
        print(f"Samsung set channel - {number}")
