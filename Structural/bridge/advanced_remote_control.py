from Structural.bridge.device import Device
from Structural.bridge.remote_control import RemoteControl


class AdvancedRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)

    def set_chanel(self, number: int):
        self._device.set_channel(number)
