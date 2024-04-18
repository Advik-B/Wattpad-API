from enum import Enum

class HTMLtags(Enum):
    paragraph = 1
    image = 2

class ParagraphAttributes(Enum):
    bold = 1
    itialic = 2

class HTML:
    data: str | bytes
    tags: HTMLtags
    attributes: ParagraphAttributes

class RenderedPage:
    title: str
    stack: list[HTML]

