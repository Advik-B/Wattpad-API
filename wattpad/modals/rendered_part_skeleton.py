from enum import Enum
from dataclasses import dataclass

class HTMLtags(Enum):
    paragraph = 1
    image = 2

@dataclass
class HTML:
    data: str
    tag: HTMLtags

@dataclass
class RenderedPage:
    title: str
    stack: list[HTML]