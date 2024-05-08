import re
from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
from sys import stdout


class HTMLtypes(Enum):
    text = 1
    image = 2


class HTMLStyle(Enum):
    general = 1
    itialic = 2
    bold = 3

@dataclass
class HTMLword:
    data: str
    style: HTMLStyle

class TextFormat:
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'

@dataclass
class HTML:
    data: list[HTMLword]
    type: HTMLtypes

    def format_for_console(self) -> str:
        s = ""
        for word in self.data:
            if word.style == HTMLStyle.bold:
                s += TextFormat.BOLD + word.data + TextFormat.RESET
            elif word.style == HTMLStyle.itialic:
                s += TextFormat.ITALIC + word.data + TextFormat.RESET
            else:
                s += word.data
        return s

    def sanitize(self) -> str:
        return "".join([word.data for word in self.data])

    def __str__(self):
        return self.sanitize()


@dataclass
class RenderedPage:
    title: str
    stack: list[HTML]

    def __getitem__(self, index):
        return self.stack[index]

    def __iter__(self):
        return iter(self.stack)

    def display(self, buffer: TextIOWrapper = stdout):
        """
        Display the rendered page in the console (using ANSI escape codes)
        Args:
            buffer: The buffer to write to. Defaults to stdout.

        Returns: None

        """
        buffer.write('=' * 80 + '\n')
        buffer.write(self.title + '\n')
        buffer.write('=' * 80 + '\n')
        buffer.write('\n')
        for line in self.stack:
            if line.type == HTMLtypes.text:
                buffer.write(line.format_for_console() + '\n')
