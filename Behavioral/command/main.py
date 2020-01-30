from Behavioral.command.black_and_white_command import BlackAndWhiteCommand
from Behavioral.command.composite_command import CompositeCommand
from Behavioral.command.resize_command import ResizeCommand

if __name__ == '__main__':
    composite = CompositeCommand()
    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())
    composite.execute()