from Structural.bridge.device import Device


class RemoteControl:

    def __init__(self, device: Device):
        self._device = device

    def turn_on(self):
        self._device.turn_on()

    def turn_off(self):
        self._device.turn_off()
