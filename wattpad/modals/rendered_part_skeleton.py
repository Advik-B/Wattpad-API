from enum import Enum
from dataclasses import dataclass
import re

class HTMLtags(Enum):
    paragraph = 1
    image = 2

@dataclass
class HTML:
    data: str
    type: HTMLtags

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
