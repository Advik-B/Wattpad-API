import re
from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
from sys import stdout


class HTMLtypes(Enum):
    text = 1
    image = 2


@dataclass
class HTML:
    data: str
    type: HTMLtypes

    def sanitized(self) -> str:
        return re.sub(r'<[^>]*>', '', self.data)


@dataclass
class RenderedPage:
    title: str
    stack: list[HTML]

    def __getitem__(self, index):
        return self.stack[index]

    def __iter__(self):
        return iter(self.stack)

    def display(self, buffer: TextIOWrapper = stdout):
        buffer.write('=' * 80 + '\n')
        buffer.write(self.title + '\n')
        buffer.write('=' * 80 + '\n')
        buffer.write('\n')
        for line in self.stack:
            if line.type == HTMLtypes.text:
                buffer.write(line.sanitized() + '\n')
