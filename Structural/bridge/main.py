from Structural.bridge.advanced_remote_control import AdvancedRemoteControl
from Structural.bridge.samsung_tv import SamsungTV
from Structural.bridge.sony_tv import SonyTV

if __name__ == '__main__':
    remote_Control = AdvancedRemoteControl(SamsungTV())
    remote_Control.turn_on()
    remote_Control.set_chanel(12)

    sony_remote_Control = AdvancedRemoteControl(SonyTV())
    sony_remote_Control.turn_on()
    sony_remote_Control.set_chanel(5)
