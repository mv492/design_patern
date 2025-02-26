import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'add')
        print(f'sub')
        print(f'multiply')
        print(f'divide')
        print(f'goodbye')
        print(f'greet')
        print(f'email')
        print(f'exit')